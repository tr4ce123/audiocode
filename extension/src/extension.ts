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


	const listen = vscode.commands.registerCommand('audiocode.listen', async () => {
		const token = uuidv4();
	  	  
		const url = `https://microphone-project.vercel.app/microphone?token=${token}`;
		await vscode.env.openExternal(vscode.Uri.parse(url));

		// TODO: whenever we open the external browser, we can immediately start polling the backend
		// using the token for the code. once we get the response with the most recently generated
		// code that is AFTER the current datetime, paste it into the editor

		async function pollApi() {
			const response = await axios.get(`https://127.0.0.1:8000/poll-data?token=${token}`);
			const transcription = response.data.transcription;
			
			if (transcription) {
				clearInterval(pollIntervalId);
				
				console.log("Receive transcription");

				const editor = vscode.window.activeTextEditor;
				if (editor) {
					const snippet = new vscode.SnippetString(transcription);
					editor.insertSnippet(snippet);
				}
			}
		}

		let pollIntervalId = setInterval(pollApi, 3000);

		setTimeout(() => {
			clearInterval(pollIntervalId);
			console.log('Stopping polling');
		}, 60000);
	});

	context.subscriptions.push(disposable);
	context.subscriptions.push(listen);
}

// This method is called when your extension is deactivated
export function deactivate() {}

