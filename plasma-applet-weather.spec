Summary:    Plasma applet that allow to see the weather	
Name:		plasma-applet-weather
Version: 	1.0.0
Release: 	%mkrel 2
Source0: 	ftp://ftp.kde.org/pub/kde/stable/4.2.0/src/extragear/%name-%version.tar.bz2
Patch0:     plasma-applet-weather-FixWithQt45.patch
License: 	GPLv2+
Group: 		Graphical desktop/KDE
Url: 		http://www.kde.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	plasma-devel
BuildRequires:  kdebase4-workspace-devel
Requires:       kdebase4-runtime
%description 
Plasma applet that allow to see the weather. 

%files
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_weather.so
%_kde_appsdir/desktoptheme/default/weather/wind-arrows.svgz
%_kde_datadir/kde4/services/plasma-applet-weather.desktop

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%{makeinstall_std} -C build

%clean
rm -rf %{buildroot}
