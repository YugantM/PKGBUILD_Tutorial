# PKGBUILD_Tutorial
tutorial for PKGBUILD scripts


# Basic Documentation for setting up a demo.

1. Install VirtualBox [Hyperlink](https://www.virtualbox.org/wiki/Downloads)
2. Download Image of ArchLinux [Hyperlink](https://www.archlinux.org/download/)
3. Setting up Virtual Box to load the iso file and get the set-up started
	
	* Click on New
	* Give the image a name
	* Memory size 4 GB(4096 MB) preferred
	* Select "Create a Virtual Hard Disk now"
	* Select VDI
	* "Dynamically Allocated"
	* Set size to 10 GB
	* Settings for Virtual Machine
		* Go to setting>>System>>Processor>>Set processors to 2 or more if you have multi cores running in the host system
		* Go to setting>>Display>>"Change scale factor to 200%" [optional setting but will help :)]
		* Go to setting>>Storage>> Give the path of .iso file to "Controller:IDE"
		* Go to setting>>Network>>Adapter1>>"Select Bridge Adapter from the dropdown of Attached to" (Enable Network Adapter)
		* Start the VM
		* Select the first option "Boot Arch Linux (x86_64)"

	* Enter the following commands:
		* To set the date and time
		```sh
		$ timedatectl set-ntp true
		```
		* To list all the partitions on the disk
		```sh
		$ lsblk
		```
		
		


	* Commands to start the SSH connection
	```sh
	$ sodu systemctl start service.sshd
	$ sodu systemctl enable service.sshd
	```
	* Above will start the connection following commands will help to check the IP address for the connection and check the connection status respectively.
	```sh
	$ IP a
	$ sodu systemctl status SSHD
	```
	* Set password for the current user[currently using root]
	```sh
	$ passwd
	```
	Enter password for the connection and re-enter to set the password.
	* Commands to connect with the SSH connection from host
	```sh
	$ ssh <user>@<IP_ADDRESS>
	```
