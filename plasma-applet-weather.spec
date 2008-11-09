Summary:        Plasma applet that allow to see the weather	
Name:		plasma-applet-weather
Version: 	0.4
Release: 	%mkrel 1
Source0: 	http://download83.mediafire.com/zb5lb332j55g/zsj2dxxj2sl/plasma-weather-%version.tar.gz
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://www.kde-look.org/content/show.php/Weather+Plasmoid?content=84251
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	plasma-devel

Requires:       kdebase4-runtime
%description 
Plasma applet that allow to see the weather. 

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_weather.so
%_kde_appsdir/desktoptheme/default/widgets/weather.svg
%_kde_datadir/kde4/services/plasma-applet-weather.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n weather

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
