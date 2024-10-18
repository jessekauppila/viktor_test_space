# 👋 Welcome to VIKTOR
Welcome to the source code of the hello-viktor app!

This demo app shows you the basics of how you can quickly set up your very own VIKTOR app. We suggest you follow along with the 
steps in the documentation, which can be found at <https://docs.viktor.ai/docs/getting-started/starter-guide/>

By following the steps, you will learn:
- the minimum file structure of any VIKTOR app
- the core of any VIKTOR app: the **editor**

## App files
The minimum file structure of a VIKTOR app looks as follows:
```
my-app
├── app.py
├── requirements.txt
└── viktor.config.toml
```

- `app.py`: this file contains the controller, and additional logic of your application.
- `requirements.txt`: all Python dependencies of your project are listed in this file.
- `viktor.config.toml`: additional configuration settings are listed in this file.

## Editor
The core of a VIKTOR app is the editor. This is the place where users can create and adjust their designs, perform calculations, and inspect results. An editor can be created by defining a so-called controller, which holds the code for:

1. **Parametrization**: the parametrization consists of the input fields, sliders, and buttons a user can interact with. These fields are available on the left-hand side of the editor.
2. **View**: a view is a visualization shown on the right-hand side of an editor. You can show 3D models, maps, graphs, reports, pictures and much more.

You will define and update your editor by adding some code to the `app.py` file.

## Further reading

More information on the fundamentals of a VIKTOR app can be found at <https://docs.viktor.ai/docs/getting-started/fundamentals/basic-app-structure/>

## About this file
This README is an optional but often included text file containing information about the app and is usually read first by developers looking for information. 
The content is up to the creator, but usually includes one or more of the following:

- A summary of the app and its functionalities.
- Installation, configuration and operating instructions.
- A list of known bugs, troubleshooting, FAQ
