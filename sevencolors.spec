Summary:	Little addicting game, take over the gaming area with your color
Summary(pl):	Uzale¿niaj±ca gra polegaj±ca na przejêciu obszaru gry swoim kolorem
Name:		sevencolors
Version:	0.80
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://digilander.iol.it/sbel/7colors/%{name}-%{version}.tar.gz
# Source0-md5:	2afdc10008ba214f8832070365410858
URL:		http://digilander.libero.it/sbel/7colors.english.html
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
7colors is a game for X Window System, for one or two players, the
goal is to color the 50% (plus one) of the rhombs on the screen,
before the other player does. Each turn the player choose a color,
this color propagates from the own corner (the lower left for player
1, the upper right for player 2) to all the neighbour rhombs with the
same color.

%description -l pl
7colors to gra dla systemu X Window, dla jednego lub dwóch graczy,
której celem jest pokolorowanie 50% (plus jednego) rombów na ekranie
zanim inny gracz zd±¿y to zrobiæ. W ka¿dej rundzie gracz wybiera
kolor, a ten kolor rozprzestrzenia siê od jego rogu (lewego dolnego
dla gracza 1, górnego prawego dla gracza 2) na wszystkie s±siednie
romby tego samego koloru.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D src/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(644,root,root,755)
%doc TODO README HISTORY
%attr(755,root,root) %{_bindir}/*
