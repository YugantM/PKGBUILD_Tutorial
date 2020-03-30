# PKGBUILD_Tutorial
tutorial for PKGBUILD scripts


# Basic Documentation for setting up a demo.

1. Install VirtualBox [Hyperlink](https://www.virtualbox.org/wiki/Downloads)
2. Download Image of ArchLinux [Hyperlink](https://www.archlinux.org/download/)
3. Setting up SSH connection from Virtual OS to host OS
	* Settings for Virtual Box
		* Go to setting>>Network>>Adapter1>>"Select Bridge Adapter from the dropdown of Attached to" (Enable Network Adapter)
		* Go to setting>>Display>>"Change scale factor to 200%" [optional setting but will help :)]
	* Commands to start the SSH connection
		* ```sh
			$ sodu systemctl start SSHD
			$ sodu systemctl enable SSHD
			```
	* Above will start the connection following commands will help to check the IP address for the connection and check the connection status respectively.
		* ```sh
			$ IP a
			$ sodu systemctl status SSHD
			```