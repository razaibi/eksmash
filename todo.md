### To build your commands for CLI:
- Add your definitions file.
- Define modes in the definitions file.
- Define actions
- Define library (file in actions folder)
- Define method for the file in the actions folder
- Define parameters to be passed.
- Create a logic file in the logic folder if needed.
- Add reference to additional logic file if needed.
- Add your custom code to be invoked in the actions file.


### To build your jinja templates
- Create file in the templates folder.
- Edit custom code in your actions folder to call the template.
- Setup any configurable/ repeatable items in the template artifacts folder.
- Setup the template inejctors folder files as Yaml
- If you want to move complex logic, move it to the template_logic folder.
- Run main app.
- Type the command to invoke the template based generation. 

# Pending
- Add @ to the YAML injectors to read from external files.
- Add $ to refer to variables in the config files.
