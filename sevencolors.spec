Summary:	Little addicting game, take over the gaming area with your color
Summary(pl.UTF-8):	Uzależniająca gra polegająca na przejęciu obszaru gry swoim kolorem
Name:		sevencolors
Version:	0.80
Release:	4
License:	GPL
Group:		X11/Applications/Games
Source0:	http://digilander.iol.it/sbel/7colors/%{name}-%{version}.tar.gz
# Source0-md5:	2afdc10008ba214f8832070365410858
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://digilander.libero.it/sbel/7colors.english.html
BuildRequires:	gnome-libs-devel
Obsoletes:	7colors
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
7colors is a game for X Window System, for one or two players, the
goal is to color the 50% (plus one) of the rhombs on the screen,
before the other player does. Each turn the player choose a color,
this color propagates from the own corner (the lower left for player
1, the upper right for player 2) to all the neighbour rhombs with the
same color.

%description -l pl.UTF-8
7colors to gra dla systemu X Window, dla jednego lub dwóch graczy,
której celem jest pokolorowanie 50% (plus jednego) rombów na ekranie
zanim inny gracz zdąży to zrobić. W każdej rundzie gracz wybiera
kolor, a ten kolor rozprzestrzenia się od jego rogu (lewego dolnego
dla gracza 1, górnego prawego dla gracza 2) na wszystkie sąsiednie
romby tego samego koloru.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO README HISTORY
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
