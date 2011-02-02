Summary:	An interactive graph visualization software
Summary(hu.UTF-8):	Egy interaktív gráf-vizualizációs szoftver
Name:		kroket
Version:	0.8.0
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://nbenoit.tuxfamily.org/projects/kroket/%{name}-%{version}.tar.bz2
# Source0-md5:	e9def3bcb329a6642453dac1956798fd
URL:		http://nbenoit.tuxfamily.org/index.php?page=Kroket
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interactive graph visualization software.

%description -l hu.UTF-8
Egy interaktív gráf-vizualizációs szoftver.

%prep
%setup -q

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install kroket $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kroket
%doc AUTHORS README doc/*.html tests
