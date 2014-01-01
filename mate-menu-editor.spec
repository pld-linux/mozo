Summary:	Mozo - menu editor for MATE desktop
Summary(pl.UTF-8):	Mozo - edytor menu dla środowiska MATE
Name:		mate-menu-editor
Version:	1.6.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	587f86b14016ca9d759b90888535c2f3
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	mate-menus-devel >= 1.1.0
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	python >= 2.4
BuildRequires:	python-pygobject >= 2.16.0
BuildRequires:	python-pygtk-devel >= 2:2.14.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme >= 0.10-3
Requires:	python-pygobject >= 2.16.0
Requires:	python-pygtk-glade >= 2:2.14.0
Requires:	python-matemenu >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mozo is a menu editor for MATE using the freedesktop.org menu
specification.

Mozo is a fork of Alacarte.

%description -l pl.UTF-8
Mozo to edytor menu dla środowiska MATE, wykorzystujący specyfikację
menu freedesktop.org.

Mozo to odgałęzienie projektu Alacarte.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=/usr/bin/python
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/io

%find_lang mozo

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f mozo.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mozo
%dir %{py_sitescriptdir}/Mozo
%{py_sitescriptdir}/Mozo/*.py[co]
%{_datadir}/mozo
%{_desktopdir}/mozo.desktop
%{_iconsdir}/hicolor/*x*/apps/mozo.png
