#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Test-CookieEmulator
Summary:	Test::Apache::CookieEmulator - test tool for Cookies without httpd
Summary(pl):	Test::Apache::CookieEmulator - narzêdzie testowe do ciasteczek bez httpd
Name:		perl-Apache-Test-CookieEmulator
Version:	0.05
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module assists authors of Apache::* modules write test suites
that would use Apache::Cookie without actually having to run and query
a server to test the cookie methods.

%description -l pl
Ten modu³ pomaga autorom modu³ów Apache::* pisaæ w³asne zestawy testów
u¿ywaj±ce Apache::Cookie bez potrzeby posiadania uruchomionego serwera
i odpytywania go, aby przetestowaæ dzia³anie ciasteczek.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%dir %{perl_sitelib}/Apache/Test
%{perl_sitelib}/Apache/Test/*.pm
%{_mandir}/man3/*
