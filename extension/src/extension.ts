// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import { v4 as uuidv4 } from 'uuid';

// This method is called when your extension is activated
// Your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "audiocode" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	const disposable = vscode.commands.registerCommand('audiocode.helloWorld', () => {
		// The code you place here will be executed every time your command is executed
		// Display a message box to the user
		vscode.window.showInformationMessage('Changed Message!');
		
		const editor = vscode.window.activeTextEditor;
		if (editor) {
			const snippet = new vscode.SnippetString("for i in range(n): \n\tprint('Hello')");
			editor.insertSnippet(snippet);
		}
	});


	const listen = vscode.commands.registerCommand('audiocode.listen', async () => {
		const token = uuidv4(); // Generate a secure random session token
	  
		// Save token somewhere if needed (e.g., in memory)
	  
		const url = `https://microphone-project.vercel.app/microphone?token=${token}`;
		await vscode.env.openExternal(vscode.Uri.parse(url));
	  });
	context.subscriptions.push(disposable);
	context.subscriptions.push(listen);
}

// This method is called when your extension is deactivated
export function deactivate() {}