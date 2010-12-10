Name:           kopete-cryptography
Version:        1.3.0
Release:        %mkrel 2
Summary:        Encrypts and signs messages in Kopete using the OpenPGP

Group:          Graphical desktop/KDE
License:        GPLv2+
URL:            http://extragear.kde.org/apps/kopete%20cryptography/
Source0:        ftp://ftp.kde.org/pub/kde/stable/4.2.3/src/extragear/%{name}-%{version}-kde4.2.3.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

buildrequires:  kdepimlibs4-devel
buildrequires:  kdenetwork4-devel
buildrequires:  kdepim4-devel
buildrequires:  gpgme-devel
buildrequires:  gettext-devel

Requires: kopete

%description
Kopete cryptography plugin encrypts and signs messages using the OpenPGP
standard. It also handles incoming messages that are encrypted or signed.


%files -f build/%{name}.lang
%defattr(-,root,root,-)
%doc COPYING COPYING.DOC COPYING.LIB
%{_kde_libdir}/kde4/kcm_kopete_cryptography.so
%{_kde_libdir}/kde4/kopete_cryptography.so
%{_kde_datadir}/kde4/services/kconfiguredialog/kopete_cryptography_config.desktop
%{_kde_datadir}/kde4/services/kopete_cryptography.desktop
%{_kde_appsdir}/kopete_cryptography/
%{_kde_docdir}/HTML/en/kopete/plugins/cryptography

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-kde4.2.3


%build
%{cmake_kde4}

%make


%install
rm -rf %{buildroot}

cd build
make DESTDIR=%buildroot install

%find_lang %name --with-html

%clean
rm -rf %{buildroot}
