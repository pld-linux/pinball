Summary:	Emilia Pinball
Summary(pl):	Pinball Emilia
Name:		pinball
Version:	0.1.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://prdownloads.sourceforge.net/pinball/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-automake.patch
URL:		http://pinball.sourceforge.net
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libltdl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
Emilia Pinball is a open source pinball game for Linux.

%description -l pl
Emilia Pinball jest otwartym pinballem dla Linuksa.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize} --ltdl
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

%{__make} check
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
ln -s %{_datadir}/pinball/pinball.xpm $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog NEWS
%attr(755,root,root) %{_bindir}/pinball
%{_datadir}/pinball
%{_includedir}/pinball
%dir %{_libdir}/pinball
%{_libdir}/pinball/*a
%attr(755,root,root) %{_libdir}/pinball/*.so*
%{_applnkdir}/Games/Arcade/*
%{_pixmapsdir}/*
