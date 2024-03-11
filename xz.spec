#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v4
# autospec commit: 1ab68ca
#
# Source0 file verified with key 0x59FCF207FEA7F445 (jiat0218@gmail.com)
#
%define keepstatic 1
Name     : xz
Version  : 5.6.1
Release  : 90
URL      : https://github.com/tukaani-project/xz/releases/download/v5.6.1/xz-5.6.1.tar.xz
Source0  : https://github.com/tukaani-project/xz/releases/download/v5.6.1/xz-5.6.1.tar.xz
Source1  : https://github.com/tukaani-project/xz/releases/download/v5.6.1/xz-5.6.1.tar.xz.sig
Summary  : General purpose data compression library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1 Public-Domain
Requires: xz-bin = %{version}-%{release}
Requires: xz-lib = %{version}-%{release}
Requires: xz-license = %{version}-%{release}
Requires: xz-locales = %{version}-%{release}
Requires: xz-man = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : openssl-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
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
4. Translations
5. Other implementations of the .xz format
6. Contact information

%package bin
Summary: bin components for the xz package.
Group: Binaries
Requires: xz-license = %{version}-%{release}

%description bin
bin components for the xz package.


%package dev
Summary: dev components for the xz package.
Group: Development
Requires: xz-lib = %{version}-%{release}
Requires: xz-bin = %{version}-%{release}
Provides: xz-devel = %{version}-%{release}
Requires: xz = %{version}-%{release}

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


%package staticdev
Summary: staticdev components for the xz package.
Group: Default
Requires: xz-dev = %{version}-%{release}

%description staticdev
staticdev components for the xz package.


%package staticdev32
Summary: staticdev32 components for the xz package.
Group: Default
Requires: xz-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the xz package.


%prep
%setup -q -n xz-5.6.1
cd %{_builddir}/xz-5.6.1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p2
pushd ..
cp -a xz-5.6.1 build32
popd
pushd ..
cp -a xz-5.6.1 buildavx2
popd
pushd ..
cp -a xz-5.6.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710167907
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%reconfigure  --enable-assume-ram=1024
make  %{?_smp_mflags}  pgo-build
pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
ASFLAGS="${CLEAR_INTERMEDIATE_ASFLAGS}${CLEAR_INTERMEDIATE_ASFLAGS:+ }--32"
CFLAGS="${CLEAR_INTERMEDIATE_CFLAGS}${CLEAR_INTERMEDIATE_CFLAGS:+ }-m32 -mstackrealign"
CXXFLAGS="${CLEAR_INTERMEDIATE_CXXFLAGS}${CLEAR_INTERMEDIATE_CXXFLAGS:+ }-m32 -mstackrealign"
LDFLAGS="${CLEAR_INTERMEDIATE_LDFLAGS}${CLEAR_INTERMEDIATE_LDFLAGS:+ }-m32 -mstackrealign"
%reconfigure  --enable-assume-ram=1024  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  pgo-build
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%reconfigure  --enable-assume-ram=1024
make  %{?_smp_mflags}  pgo-build
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
GOAMD64=v4
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -mprefer-vector-width=256 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v4 "
%reconfigure  --enable-assume-ram=1024
make  %{?_smp_mflags}  pgo-build
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :
cd ../buildavx512;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710167907
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xz
cp %{_builddir}/xz-%{version}/COPYING.GPLv2 %{buildroot}/usr/share/package-licenses/xz/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/xz-%{version}/COPYING.GPLv3 %{buildroot}/usr/share/package-licenses/xz/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/xz-%{version}/COPYING.LGPLv2.1 %{buildroot}/usr/share/package-licenses/xz/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
export GOAMD64=v2
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v4
pushd ../buildavx512/
%make_install_v4
popd
GOAMD64=v2
%make_install
%find_lang xz
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/lzmadec
/V3/usr/bin/lzmainfo
/V3/usr/bin/xz
/V3/usr/bin/xzdec
/V4/usr/bin/lzmadec
/V4/usr/bin/lzmainfo
/V4/usr/bin/xz
/V4/usr/bin/xzdec
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
/usr/include/lzma.h
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
/usr/lib64/liblzma.so
/usr/lib64/pkgconfig/liblzma.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/liblzma.so
/usr/lib32/pkgconfig/32liblzma.pc
/usr/lib32/pkgconfig/liblzma.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/xz/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/liblzma.so.5.6.1
/V4/usr/lib64/liblzma.so.5.6.1
/usr/lib64/liblzma.so.5
/usr/lib64/liblzma.so.5.6.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/liblzma.so.5
/usr/lib32/liblzma.so.5.6.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xz/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/xz/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/xz/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/de/man1/lzcat.1
/usr/share/man/de/man1/lzcmp.1
/usr/share/man/de/man1/lzdiff.1
/usr/share/man/de/man1/lzegrep.1
/usr/share/man/de/man1/lzfgrep.1
/usr/share/man/de/man1/lzgrep.1
/usr/share/man/de/man1/lzless.1
/usr/share/man/de/man1/lzma.1
/usr/share/man/de/man1/lzmadec.1
/usr/share/man/de/man1/lzmainfo.1
/usr/share/man/de/man1/lzmore.1
/usr/share/man/de/man1/unlzma.1
/usr/share/man/de/man1/unxz.1
/usr/share/man/de/man1/xz.1
/usr/share/man/de/man1/xzcat.1
/usr/share/man/de/man1/xzcmp.1
/usr/share/man/de/man1/xzdec.1
/usr/share/man/de/man1/xzdiff.1
/usr/share/man/de/man1/xzegrep.1
/usr/share/man/de/man1/xzfgrep.1
/usr/share/man/de/man1/xzgrep.1
/usr/share/man/de/man1/xzless.1
/usr/share/man/de/man1/xzmore.1
/usr/share/man/fr/man1/lzcat.1
/usr/share/man/fr/man1/lzless.1
/usr/share/man/fr/man1/lzma.1
/usr/share/man/fr/man1/lzmadec.1
/usr/share/man/fr/man1/lzmainfo.1
/usr/share/man/fr/man1/unlzma.1
/usr/share/man/fr/man1/unxz.1
/usr/share/man/fr/man1/xz.1
/usr/share/man/fr/man1/xzcat.1
/usr/share/man/fr/man1/xzdec.1
/usr/share/man/fr/man1/xzless.1
/usr/share/man/ko/man1/lzcat.1
/usr/share/man/ko/man1/lzcmp.1
/usr/share/man/ko/man1/lzdiff.1
/usr/share/man/ko/man1/lzegrep.1
/usr/share/man/ko/man1/lzfgrep.1
/usr/share/man/ko/man1/lzgrep.1
/usr/share/man/ko/man1/lzless.1
/usr/share/man/ko/man1/lzma.1
/usr/share/man/ko/man1/lzmadec.1
/usr/share/man/ko/man1/lzmainfo.1
/usr/share/man/ko/man1/lzmore.1
/usr/share/man/ko/man1/unlzma.1
/usr/share/man/ko/man1/unxz.1
/usr/share/man/ko/man1/xz.1
/usr/share/man/ko/man1/xzcat.1
/usr/share/man/ko/man1/xzcmp.1
/usr/share/man/ko/man1/xzdec.1
/usr/share/man/ko/man1/xzdiff.1
/usr/share/man/ko/man1/xzegrep.1
/usr/share/man/ko/man1/xzfgrep.1
/usr/share/man/ko/man1/xzgrep.1
/usr/share/man/ko/man1/xzless.1
/usr/share/man/ko/man1/xzmore.1
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
/usr/share/man/pt_BR/man1/lzcat.1
/usr/share/man/pt_BR/man1/lzless.1
/usr/share/man/pt_BR/man1/lzma.1
/usr/share/man/pt_BR/man1/lzmadec.1
/usr/share/man/pt_BR/man1/lzmainfo.1
/usr/share/man/pt_BR/man1/unlzma.1
/usr/share/man/pt_BR/man1/unxz.1
/usr/share/man/pt_BR/man1/xz.1
/usr/share/man/pt_BR/man1/xzcat.1
/usr/share/man/pt_BR/man1/xzdec.1
/usr/share/man/pt_BR/man1/xzless.1
/usr/share/man/ro/man1/lzcat.1
/usr/share/man/ro/man1/lzcmp.1
/usr/share/man/ro/man1/lzdiff.1
/usr/share/man/ro/man1/lzegrep.1
/usr/share/man/ro/man1/lzfgrep.1
/usr/share/man/ro/man1/lzgrep.1
/usr/share/man/ro/man1/lzless.1
/usr/share/man/ro/man1/lzma.1
/usr/share/man/ro/man1/lzmadec.1
/usr/share/man/ro/man1/lzmainfo.1
/usr/share/man/ro/man1/lzmore.1
/usr/share/man/ro/man1/unlzma.1
/usr/share/man/ro/man1/unxz.1
/usr/share/man/ro/man1/xz.1
/usr/share/man/ro/man1/xzcat.1
/usr/share/man/ro/man1/xzcmp.1
/usr/share/man/ro/man1/xzdec.1
/usr/share/man/ro/man1/xzdiff.1
/usr/share/man/ro/man1/xzegrep.1
/usr/share/man/ro/man1/xzfgrep.1
/usr/share/man/ro/man1/xzgrep.1
/usr/share/man/ro/man1/xzless.1
/usr/share/man/ro/man1/xzmore.1
/usr/share/man/uk/man1/lzcat.1
/usr/share/man/uk/man1/lzcmp.1
/usr/share/man/uk/man1/lzdiff.1
/usr/share/man/uk/man1/lzegrep.1
/usr/share/man/uk/man1/lzfgrep.1
/usr/share/man/uk/man1/lzgrep.1
/usr/share/man/uk/man1/lzless.1
/usr/share/man/uk/man1/lzma.1
/usr/share/man/uk/man1/lzmadec.1
/usr/share/man/uk/man1/lzmainfo.1
/usr/share/man/uk/man1/lzmore.1
/usr/share/man/uk/man1/unlzma.1
/usr/share/man/uk/man1/unxz.1
/usr/share/man/uk/man1/xz.1
/usr/share/man/uk/man1/xzcat.1
/usr/share/man/uk/man1/xzcmp.1
/usr/share/man/uk/man1/xzdec.1
/usr/share/man/uk/man1/xzdiff.1
/usr/share/man/uk/man1/xzegrep.1
/usr/share/man/uk/man1/xzfgrep.1
/usr/share/man/uk/man1/xzgrep.1
/usr/share/man/uk/man1/xzless.1
/usr/share/man/uk/man1/xzmore.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/liblzma.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/liblzma.a

%files locales -f xz.lang
%defattr(-,root,root,-)

