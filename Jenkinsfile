pipeline{
	agent any 

stages{
	
	stage('Build'){
		steps{
			sh 'pwd'
			echo 'desplaying the repo'			
			sh 'ls ./add_PKGBUILD'
			sh 'ls'
			sh 'makepkg'		}
	}

}

}