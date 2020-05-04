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
		* To manipulate the partition
		```sh
		$ fdisk /dev/sda
		```		
		* To create a DOS disklabel
		```sh
		$ o <ENTER>
		```
		* To create a new partition
		```sh
		$ n <ENTER>
		```		
		* To set the new partition as primary partition
		```sh
		$ p <ENTER>
		```
		* Set partition number to 1
		```sh
		$ 1 <ENTER>
		$ <ENTER>
		```
		* Set size of partition to 200MB
		```sh
		$ +200M <ENTER>
		```
		* Make the partition bootable
		```sh
		$ a <ENTER>
		```
		* To create a new partition
		```sh
		$ n <ENTER>
		```		
		* To set the new partition as primary partition
		```sh
		$ p <ENTER>
		```
		* Set partition number to 2
		```sh
		$ 2 <ENTER>
		$ <ENTER>
		$ <ENTER> # to set the rest of the memory to this partition (default)
		```
		* To alter the partition table
		```sh
		$ w <ENTER>
		```
		* Format both the partitions
		```sh
		$ mkfs.ext4 /dev/sda1 <ENTER>
		$ mkfs.ext4 /dev/sda2 <ENTER>
		```
		* Before mounting the partitions create required directories
		```sh
		$ mkdir /mnt/boot /mnt/home <ENTER>
		```
		* Mount both the partitions
		```sh
		$ mount /dev/sda2 /mnt <ENTER>
		$ mount /dev/sda1 /mnt/boot <ENTER>
		```
		* To install arch in the VDI
		```sh
		$ pacstrap base base-devel <ENTER> 
		# base is for installing arch 
		# base-devel is for installing the development tools for the arch
		```
		* To generate [fsab](https://www.archlinux.org/download/) file
		```sh
		$ genfstab -U /mnt >> /mnt/etc/fstab <ENTER>		
		```
		* Switching the root to the VDI
		```sh
		$ arch-chroot /mnt <ENTER>		
		```
		* Install mkinitcpio 
		```sh
		$ pacman -Sy mkinitcpio <ENTER>		
		```
		* Install linux and linux-firmware 
		```sh
		$ pacman -Sy linux <ENTER>	
		$ pacman -Sy linux-firmware <ENTER>	
		```
		* To create initial RAM disk
		```sh
		$ mkinitcpio -p linux<ENTER>	
		```
		* To install grub
		```sh
		$ pacman -S grub<ENTER>	
		```
		* Switch to primary Arch-Linux
		```sh
		$ grub-install --target=i386-pc /dev/sda<ENTER>	
		```
		* Configure grub
		```sh
		$ grub-mkconfig -o /boot/grub/grub.cfg<ENTER>	
		```
		* Set password
		```sh
		$ passwd<ENTER>	
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
