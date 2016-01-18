#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xz
Version  : 5.2.2
Release  : 32
URL      : http://tukaani.org/xz/xz-5.2.2.tar.gz
Source0  : http://tukaani.org/xz/xz-5.2.2.tar.gz
Summary  : General purpose data compression library
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1 Public-Domain
Requires: xz-bin
Requires: xz-lib
Requires: xz-doc
Requires: xz-locales
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
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

%description bin
bin components for the xz package.


%package dev
Summary: dev components for the xz package.
Group: Development
Requires: xz-lib
Requires: xz-bin
Provides: xz-devel

%description dev
dev components for the xz package.


%package doc
Summary: doc components for the xz package.
Group: Documentation

%description doc
doc components for the xz package.


%package lib
Summary: lib components for the xz package.
Group: Libraries

%description lib
lib components for the xz package.


%package locales
Summary: locales components for the xz package.
Group: Default

%description locales
locales components for the xz package.


%prep
%setup -q -n xz-5.2.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2

%build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export CFLAGS="$CFLAGS -ffunction-sections -falign-functions=32 -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -ffunction-sections -falign-functions=32 -O3 -flto -fno-semantic-interposition "
%reconfigure --disable-static --enable-assume-ram=1024
make V=1  %{?_smp_mflags} pgo-build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang xz

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/xz/*
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*

%files locales -f xz.lang 
%defattr(-,root,root,-)

