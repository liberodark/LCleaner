# Maintainer: liberodark

pkgname=lcleaner
pkgver=1.0.0
pkgrel=1
pkgdesc="Clean your Linux system with ease"
arch=('x86_64')
license=('GPL3')
url="https://github.com/liberodark/LCleaner"
depends=('tk' 'python-pillow' 'python' 'polkit')
install=lcleaner.install
source=("lcleaner.py"
        "lcleaner.png"
        "lcleaner.desktop"
        "org.lcleaner.policy")

sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

package() {
    install -Dm755 "lcleaner.py" "${pkgdir}/usr/bin/lcleaner.py"
    install -Dm644 "lcleaner.desktop" "${pkgdir}/usr/share/applications/lcleaner.desktop"
    install -Dm644 "lcleaner.png" "${pkgdir}/usr/share/icons/hicolor/128x128/apps/lcleaner.png"
    install -Dm644 "org.lcleaner.policy" "${pkgdir}/usr/share/polkit-1/actions/org.lcleaner.policy"

    mkdir -p "${pkgdir}/usr/bin"
    ln -s "/usr/bin/lcleaner.py" "${pkgdir}/usr/bin/lcleaner"
}
