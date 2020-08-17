pipeline{
	agent any 

stages{
	
	stage('Build'){
		steps{
			sh 'pwd'
			echo 'desplaying the repo'
			sh 'cd ./add_PKGBUILD/'
			sh 'makepkg'		}
	}

}

}