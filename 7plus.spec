Summary:	Application to split binary files - used widely by hams
Summary(pl):	Programik do dzielenia plikow binarnych - uzywany przez radioamatorów
Name:		7plus
Version:	2.25
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	ftp://excelsior.kullen.rwth-aachen.de/pub/packet_radio/misc/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Application to split binary files - like base64 / uuencode but for
hams.

%description -l pl
Program pozwalajacy dzielic binaria - jak base64 czy uuencode, lecz
jest powszechnie stosowany przez radioamatorów.

%prep
%setup -q -n 7plsrc.225

%build
mv linux.mak Makefile
%{__make} CC="gcc %{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}

install 7plus		$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/7plus
