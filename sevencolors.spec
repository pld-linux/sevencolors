Summary:	Little addicting game, take over the gaming area with your color
Name:		7colors
%define _name	sevencolors
Version:	0.80
Release:	0.1
Source0:	http://digilander.iol.it/sbel/7colors/%{_name}-%{version}.tar.bz2
# Source0-md5:	a6b789ceae0f65657d69a95499923631
URL:		http://digilander.libero.it/sbel/7colors.english.html
License:	GPL
Group:		X11/Applications/Games
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-libs
BuildRequires:	esound-devel
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel 
BuildRequires:	audiofile-devel
BuildRequires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
7colors is a game for XWindow, for one or two players, the goal is to
color the 50% (plus one) of the rhombs on the screen, before the other
player does. Each turn the player choose a color, this color
propagates from the own corner (the lower left for player 1, the upper
right for player 2) to all the neighbour rhombs with the same color.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D src/%{_name} $RPM_BUILD_ROOT%{_bindir}/%{_name}

%files
%defattr(644,root,root,755)
%doc TODO README HISTORY
%attr(755,root,root) %{_bindir}/*
