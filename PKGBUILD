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
	"org.lcleaner.policy")

sha256sums=('98c83230d1db982f4864660e83e8d6de6cce14ad85d33e2594ca8bf62107a1e7'
            '08797be12a2e46ae358819ce6f439bcac2dbc28da6f3c6db43c6ec766cdb08be'
            '005ecd297028b12cda1c413fe5ca20fdeadb96901f4f79ead315cd7ad38c972f'
            '3dc6506ad5f5f6246ef51dd88bae758d144b7d7b2ff7c017f798ce18226e53db')		

package() {
        install -Dm644 "lcleaner.desktop" "${pkgdir}/usr/share/applications/lcleaner.desktop"
        install -Dm644 "lcleaner.py" "${pkgdir}/usr/bin/lcleaner.py"
        install -Dm644 "lcleaner.png" "${pkgdir}/usr/share/icons/lcleaner.png"
        install -Dm644 "org.lcleaner.policy" "${pkgdir}/usr/share/polkit-1/actions/org.lcleaner.policy"
} 

