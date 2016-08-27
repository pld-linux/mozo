Summary:	Mozo - menu editor for MATE desktop
Summary(pl.UTF-8):	Mozo - edytor menu dla środowiska MATE
Name:		mozo
Version:	1.14.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.14/%{name}-%{version}.tar.xz
# Source0-md5:	573bf9df46e7d42e0f0f615e90bad0dc
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	gettext-tools
BuildRequires:	intltool >= 0.40.0
BuildRequires:	mate-menus-devel >= 1.1.0
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	python >= 1:2.7
BuildRequires:	python-pygobject3 >= 3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme >= 0.10-3
Requires:	gdk-pixbuf2
Requires:	gobject-introspection
Requires:	gtk+3 >= 3.0
Requires:	python-pygobject3 >= 3.0
Requires:	python-matemenu >= 1.1.0
Obsoletes:	mate-menu-editor
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
	PYTHON=/usr/bin/python \
	am_cv_python_pythondir=%{py_sitescriptdir} \
	--disable-icon-update \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ku_IQ,pms}

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
%{_mandir}/man1/mozo.1*
