%define _name sevencolors
Summary:	Little addicting game, take over the gaming area with your color
Name:		7colors
Version:	0.80
Release:	0.1
Source0:	http://digilander.iol.it/sbel/7colors/%{_name}-%{version}.tar.bz2
# Source0-md5:	a6b789ceae0f65657d69a95499923631
URL:		http://digilander.libero.it/sbel/7colors.english.html
License:	GPL
Group:		Applications/Games/Boards

# Automatically added by buildreq on Thu Jan 09 2003
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-libs
BuildRequires:	esound-devel
BuildRequires:	glib-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel 
BuildRequires:	audiofile-devel
#BuildRequires:	libdb1-devel
BuildRequires:	xpm-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
7colors is a game for XWindow, for one or two players, the goal is to
color the 50% (plus one) of the rhombs on the screen, before the other
player does. Each turn the player choose a color, this color
propagates from the own corner (the lower left for player 1, the upper
right for player 2) to all the neighbour rhombs with the same color.

%prep
%setup -n %{_name}-%{version} -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D src/%{_name} $RPM_BUILD_ROOT%{_bindir}/%{_name}

#install -D %SOURCE4 $RPM_BUILD_ROOT%_menudir/%name
#install -D %SOURCE6 $RPM_BUILD_ROOT%_iconsdir/%name.xpm
#install -D %SOURCE5 $RPM_BUILD_ROOT%_miconsdir/%name.xpm
#install -D %SOURCE7 $RPM_BUILD_ROOT%_liconsdir/%name.xpm

%files
%defattr(644,root,root,755)
%doc TODO README HISTORY
%{_bindir}/*

# end of file
