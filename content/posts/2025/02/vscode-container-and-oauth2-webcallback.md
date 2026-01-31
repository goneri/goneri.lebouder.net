+++
title = "VSCode container and OAuth2 Web callback"
date = 2025-02-03T16:59:14+00:00
[taxonomies]
tags = ["tips", "linux", "containers"]
+++
I use Fedora Silverblue and my VSCode runs inside a container. I manage the container with the "toolbox" CLI tool. I also, to get the last version of Firefox, I use it's upstream Flatpak To be able to get VSCode's OAuth2 callback to work properly, I had to do a bit of extra configuration.

You need a .desktop file to overload VSCode's default way to open web URL. We don't want to rely on the default xdg-open configuration (e.g: xdg-open http://www.google.com) which would otherwise try to open up a a new web browser INSIDE the container.

Prepare the code-url-handler.desktop file, you need to adjust the Exec to prefix the command with the toolbox run call:

```ini
[Desktop Entry]
Name=Visual Studio Code - URL Handler
Comment=Code Editing. Redefined.
GenericName=Text Editor
Exec=toolbox run --container vscode /usr/share/code/code --open-url %U
Icon=vscode
Type=Application
NoDisplay=true
StartupNotify=true
Categories=Utility;TextEditor;Development;IDE;
MimeType=x-scheme-handler/vscode;
Keywords=vscode;
```

The goal here is to be sure we send back the vscode:// link to the correct instance of VSCode (within the container!).

To install the .desktop, run these commands in your system (not in a container).

```
desktop-file-install --dir=$HOME/.local/share/applications code-url-handler.desktop
```

And refresh the local cache:

```
update-desktop-database ~/.local/share/applications
```

Inside the container we need to also install flatpak-xdg-utils and use it instead of the default /usr/bin/xdg-open. This way your containerize VSCode will be able to open the web page inisde yet another container (the Flatpak app). This is a snippet of my Containerfile of my VSCode container:

```
RUN dnf install -y flatpak-xdg-utils
RUN ln -sf /usr/bin/flatpak-xdg-open /usr/bin/xdg-open
```

See: [https://github.com/microsoft/vscode-pull-request-github/issues/3472#issuecomment-1825008268](https://github.com/microsoft/vscode-pull-request-github/issues/3472#issuecomment-1825008268)
