# Maintainer: liberodark

pkgname=lcleaner
pkgver=0.0.1
pkgrel=1
pkgdesc="Clean your Linux"
arch=('x86_64')
license=('GPL3')
url="https://github.com/liberodark/LCleaner"
depends=('tk' 'python-pillow')
install=lcleaner.install
source=("lcleaner.py"
        "lcleaner.png"
        "lcleaner.desktop"
        "lcleaner.conf"
	"org.lcleaner.policy")

sha256sums=('4fe1b85883adcccccf05e30756d68c60859db18ec760d22f8ea24d78690a4496'
            '874700067f446dff59f8e4e6c3b14519ca8afdf31742af629343c80002c71376'
            'c5dbfca766050bdbfd36866c1f479ca8039aae80fa8b2847b376c05087d1364c'
            'd8fafeb25a8b2368803565ed62ba147aa38adfe57089fe44125f5e07eea3d21b'
            'dcf05a9d8c5cfe2cc23523eaab9bbd30932b3d2c68ad8d38edbdcad372053920')		

package() {
        install -Dm644 "lcleaner.desktop" "${pkgdir}/usr/share/applications/lcleaner.desktop"
        install -Dm644 "lcleaner.py" "${pkgdir}/usr/bin/lcleaner.py"
        install -Dm644 "lcleaner.png" "${pkgdir}/usr/share/icons/lcleaner.png"
        install -Dm644 "org.lcleaner.policy" "${pkgdir}/usr/share/polkit-1/actions/org.lcleaner.policy"
} 

