%define realname   VCP
%define date 20050110

%define tar_name %{realname}-autrijus-snapshot-%{version}-%{date}

Name:		perl-%{realname}
Version:	0.9
Release:	%mkrel 0.autrijus.%{date}.4
License:	BSD
Group:		Development/Perl
Summary:    	Perl modules to copy ressources between cvs, p4 and RevML
# http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/VCP-autrijus-snapshot-0.9-20050110.tar.gz
Source0:    	%{tar_name}.tar.bz2
Url:		http://www.cpan.org
BuildRequires:  perl-HTML-Tree 
BuildRequires:  perl-IPC-Run3 
BuildRequires:  perl-XML-AutoWriter 
BuildRequires:  perl-Text-Diff
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-Regexp-Shellish
BuildArch:      noarch
%description

vcp (and the Perl module VCP.pm) is a system for copying resources
under version control between repositories. cvs, p4 and RevML files
are currently supported.

vcp can re-root directory hierarchies diring the transfer, and,
using source specifications, or by filtering RevML files, subsets of
files and revisions may be copied.

Both whole-repository and incremental updates are supported.

%prep
%setup -q -n %{tar_name}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make
%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc LICENSE CHANGES README 
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man3/*
%{_mandir}/man1/*

