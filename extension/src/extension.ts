// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import { v4 as uuidv4 } from 'uuid';
import axios from 'axios';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	console.log('Congratulations, your extension "audiocode" is now active!');

	const disposable = vscode.commands.registerCommand('audiocode.helloWorld', () => {
		vscode.window.showInformationMessage('Changed Message!');
		
		const editor = vscode.window.activeTextEditor;
		if (editor) {
			const snippet = new vscode.SnippetString("for i in range(n): \n\tprint('Hello')");
			editor.insertSnippet(snippet);
		}
	});

	let pollIntervalId: NodeJS.Timeout | undefined = undefined;

	const listen = vscode.commands.registerCommand('audiocode.listen', async () => {
		const token = uuidv4();
		const url = `https://microphone-project.vercel.app/microphone?token=${token}`;
		await vscode.env.openExternal(vscode.Uri.parse(url));

		async function pollApi() {
			console.log("Poll Called");
			try {
				const response = await axios.get(`http://127.0.0.1:8000/poll-data/${token}`);
				const { code, line_number } = response.data;
				console.log(code, line_number);
				
				if (code) {					
					console.log("Received transcription");
					const editor = vscode.window.activeTextEditor;
					if (editor) {
						let processedCode = code.replace(/\\n/g, "\n");
						const doc = editor.document;
						const totalLines = doc.lineCount;
						const isEmptyDoc = totalLines === 1 && doc.lineAt(0).text.trim() === "";

						let insertLine = isEmptyDoc ? 0 : totalLines - 1;
						if (line_number !== null) {
							insertLine = Math.min(Math.max(0, line_number), totalLines - 1);
						}

						const position = isEmptyDoc
							? new vscode.Position(0, 0)
							: doc.lineAt(insertLine).range.end;

						let baseIndent = "";
						for (let i = insertLine - 1; i >= 0; i--) {
							const text = doc.lineAt(i).text;
							if (!text.trim()) {continue;}
							const m = text.match(/^(\s*)/);
							if (m && m[1].length > 0) {             
								baseIndent = m[1];
								break;
							}
						}
						console.log(`🔍 detected indent (${baseIndent.length} spaces): '${baseIndent}'`);

						const snippetBody = processedCode
							.split("\n")
							.map((ln: string, idx: number) => idx === 0 ? ln : baseIndent + ln)
							.join("\n") + "\n";

						await editor.insertSnippet(new vscode.SnippetString(snippetBody), position);
						await vscode.commands.executeCommand('editor.action.formatDocument');
					}
				}
			} catch (e) {
				console.error("Polling error", e);
			}
		}

		pollIntervalId = setInterval(pollApi, 3000);
	});

	const stopListening = vscode.commands.registerCommand('audiocode.stopListening', () => {
		if (pollIntervalId) {
			clearInterval(pollIntervalId);
			pollIntervalId = undefined;
			console.log('Stopped polling');
		}
	});

	context.subscriptions.push(disposable);
	context.subscriptions.push(listen);
	context.subscriptions.push(stopListening);
}

// This method is called when your extension is deactivated
export function deactivate() {}

