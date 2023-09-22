Name     : grim
Version  : 1.4.1
Release  : 1
URL      : https://github.com/emersion/grim
Source0  : https://git.sr.ht/~emersion/grim/refs/download/v%{version}/grim-%{version}.tar.gz
Summary:   Utility program for screen recording of wlroots-based compositors
Group    : Development/Tools
License  : MIT
Requires : sway
BuildRequires :  meson cmake
BuildRequires :  pkgconfig(scdoc)  
BuildRequires :  pkgconfig(wayland-client)
BuildRequires :  pkgconfig(wayland-cursor)
BuildRequires :  pkgconfig(wayland-protocols)
BuildRequires :  pkgconfig(libjpeg)
BuildRequires :  pkgconfig(libpng)
BuildRequires :  pkgconfig(pixman-1)

%description
Utility program for screen recording of wlroots-based compositors

%prep
%setup -q -n grim-%{version}

%build
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain  builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/grim
