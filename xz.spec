#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x38EE757D69184620 (lasse.collin@tukaani.org)
#
Name     : xz
Version  : 5.2.4
Release  : 51
URL      : http://tukaani.org/xz/xz-5.2.4.tar.gz
Source0  : http://tukaani.org/xz/xz-5.2.4.tar.gz
Source99 : http://tukaani.org/xz/xz-5.2.4.tar.gz.sig
Summary  : General purpose data compression library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1 Public-Domain
Requires: xz-bin = %{version}-%{release}
Requires: xz-lib = %{version}-%{release}
Requires: xz-license = %{version}-%{release}
Requires: xz-locales = %{version}-%{release}
Requires: xz-man = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : gettext-bin
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : openssl-dev
BuildRequires : pkg-config-dev
Patch1: default-threading.patch
Patch2: io-size.patch
Patch3: speedup.patch
Patch4: add-pgo.patch

%description
XZ Utils
========
0. Overview
1. Documentation
1.1. Overall documentation
1.2. Documentation for command-line tools
1.3. Documentation for liblzma
2. Version numbering
3. Reporting bugs
4. Translating the xz tool
5. Other implementations of the .xz format
6. Contact information

%package bin
Summary: bin components for the xz package.
Group: Binaries
Requires: xz-license = %{version}-%{release}
Requires: xz-man = %{version}-%{release}

%description bin
bin components for the xz package.


%package dev
Summary: dev components for the xz package.
Group: Development
Requires: xz-lib = %{version}-%{release}
Requires: xz-bin = %{version}-%{release}
Provides: xz-devel = %{version}-%{release}

%description dev
dev components for the xz package.


%package dev32
Summary: dev32 components for the xz package.
Group: Default
Requires: xz-lib32 = %{version}-%{release}
Requires: xz-bin = %{version}-%{release}
Requires: xz-dev = %{version}-%{release}

%description dev32
dev32 components for the xz package.


%package doc
Summary: doc components for the xz package.
Group: Documentation
Requires: xz-man = %{version}-%{release}

%description doc
doc components for the xz package.


%package lib
Summary: lib components for the xz package.
Group: Libraries
Requires: xz-license = %{version}-%{release}

%description lib
lib components for the xz package.


%package lib32
Summary: lib32 components for the xz package.
Group: Default
Requires: xz-license = %{version}-%{release}

%description lib32
lib32 components for the xz package.


%package license
Summary: license components for the xz package.
Group: Default

%description license
license components for the xz package.


%package locales
Summary: locales components for the xz package.
Group: Default

%description locales
locales components for the xz package.


%package man
Summary: man components for the xz package.
Group: Default

%description man
man components for the xz package.


%prep
%setup -q -n xz-5.2.4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
pushd ..
cp -a xz-5.2.4 build32
popd
pushd ..
cp -a xz-5.2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542435458
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%reconfigure --disable-static --enable-assume-ram=1024
make  %{?_smp_mflags} pgo-build
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="$ASFLAGS --32"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%reconfigure --disable-static --enable-assume-ram=1024  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags} pgo-build
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%reconfigure --disable-static --enable-assume-ram=1024
make  %{?_smp_mflags} pgo-build
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../buildavx2;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1542435458
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xz
cp COPYING %{buildroot}/usr/share/package-licenses/xz/COPYING
cp COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/xz/COPYING.GPLv2
cp COPYING.GPLv3 %{buildroot}/usr/share/package-licenses/xz/COPYING.GPLv3
cp COPYING.LGPLv2.1 %{buildroot}/usr/share/package-licenses/xz/COPYING.LGPLv2.1
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
%find_lang xz

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/haswell/lzcat
%exclude /usr/bin/haswell/lzma
%exclude /usr/bin/haswell/lzmadec
%exclude /usr/bin/haswell/lzmainfo
%exclude /usr/bin/haswell/unlzma
%exclude /usr/bin/haswell/unxz
%exclude /usr/bin/haswell/xz
%exclude /usr/bin/haswell/xzcat
%exclude /usr/bin/haswell/xzdec
/usr/bin/lzcat
/usr/bin/lzcmp
/usr/bin/lzdiff
/usr/bin/lzegrep
/usr/bin/lzfgrep
/usr/bin/lzgrep
/usr/bin/lzless
/usr/bin/lzma
/usr/bin/lzmadec
/usr/bin/lzmainfo
/usr/bin/lzmore
/usr/bin/unlzma
/usr/bin/unxz
/usr/bin/xz
/usr/bin/xzcat
/usr/bin/xzcmp
/usr/bin/xzdec
/usr/bin/xzdiff
/usr/bin/xzegrep
/usr/bin/xzfgrep
/usr/bin/xzgrep
/usr/bin/xzless
/usr/bin/xzmore

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/lzma/base.h
/usr/include/lzma/bcj.h
/usr/include/lzma/block.h
/usr/include/lzma/check.h
/usr/include/lzma/container.h
/usr/include/lzma/delta.h
/usr/include/lzma/filter.h
/usr/include/lzma/hardware.h
/usr/include/lzma/index.h
/usr/include/lzma/index_hash.h
/usr/include/lzma/lzma12.h
/usr/include/lzma/stream_flags.h
/usr/include/lzma/version.h
/usr/include/lzma/vli.h
/usr/lib64/haswell/liblzma.so
/usr/lib64/liblzma.so
/usr/lib64/pkgconfig/liblzma.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/liblzma.so
/usr/lib32/pkgconfig/32liblzma.pc
/usr/lib32/pkgconfig/liblzma.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/xz/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/liblzma.so.5
/usr/lib64/haswell/liblzma.so.5.2.4
/usr/lib64/liblzma.so.5
/usr/lib64/liblzma.so.5.2.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/liblzma.so.5
/usr/lib32/liblzma.so.5.2.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xz/COPYING
/usr/share/package-licenses/xz/COPYING.GPLv2
/usr/share/package-licenses/xz/COPYING.GPLv3
/usr/share/package-licenses/xz/COPYING.LGPLv2.1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/lzcat.1
/usr/share/man/man1/lzcmp.1
/usr/share/man/man1/lzdiff.1
/usr/share/man/man1/lzegrep.1
/usr/share/man/man1/lzfgrep.1
/usr/share/man/man1/lzgrep.1
/usr/share/man/man1/lzless.1
/usr/share/man/man1/lzma.1
/usr/share/man/man1/lzmadec.1
/usr/share/man/man1/lzmainfo.1
/usr/share/man/man1/lzmore.1
/usr/share/man/man1/unlzma.1
/usr/share/man/man1/unxz.1
/usr/share/man/man1/xz.1
/usr/share/man/man1/xzcat.1
/usr/share/man/man1/xzcmp.1
/usr/share/man/man1/xzdec.1
/usr/share/man/man1/xzdiff.1
/usr/share/man/man1/xzegrep.1
/usr/share/man/man1/xzfgrep.1
/usr/share/man/man1/xzgrep.1
/usr/share/man/man1/xzless.1
/usr/share/man/man1/xzmore.1

%files locales -f xz.lang
%defattr(-,root,root,-)

