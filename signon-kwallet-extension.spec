#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:        KWallet integration for Sign-on framework
Name:           signon-kwallet-extension
Version:	26.04.1
Release:	%{?git:0.%{git}.}1
License:        GPLv2+
Group:          System/Base
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/signon-kwallet-extension/-/archive/%{gitbranch}/signon-kwallet-extension-%{gitbranchd}.tar.bz2#/signon-kwallet-extension-%{git}.tar.bz2
%else
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/signon-kwallet-extension-%{version}.tar.xz
%endif
URL:            https://www.kde.org/
BuildRequires:  cmake(ECM)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(SignOnExtension)
BuildRequires:	cmake(KF6Wallet)
%define keyringkwallet_major 16
%define oldlibkeyringkwallet %mklibname keyring-kwallet %{keyringkwallet_major}
# The > here is not a typo -- we mean to obsolete the Plasma 6 version
# but not the Plasma 5 compat version
Obsoletes:	%{oldlibkeyringkwallet} > 24.0.0

#BuildRequires:  kwallet-devel >= 6.0

%rename plasma6-signon-kwallet-extension

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption:	-DQT_MAJOR_VERSION=6

%description
KWallet integration for Sign-on framework.

%files
%{_libdir}/signon/extensions/libkeyring-kwallet.so
