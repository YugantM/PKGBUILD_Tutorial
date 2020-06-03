pkgname=calc
pkgver=1.0
pkgrel=1
pkgdesc=""
arch=("any")
url=""
license=('GPL')
#source=("https://github.com/YugantM/Calc_package.git")
makedepends=('cmake' 'git')
_dir=${pkgname}
source=("${_dir}"::"git+https://github.com/YugantM/Calc_package.git")
#noextract=()
md5sums=('SKIP')
#md5sums=() #autofill using updpkgsums

build() {

#  ./configure --prefix=/usr 

  # create build-directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build 

  cmake ${srcdir}/$pkgname \
        -DCMAKE_INSTALL_PREFIX=/usr
  make
}

package() {
#  cd "$pkgname-$pkgver"
  cd "${srcdir}/build"
  make DESTDIR="$pkgdir/" install
}
