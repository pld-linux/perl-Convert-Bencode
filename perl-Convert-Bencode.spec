#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	Bencode
Summary:	Convert::Bencode - Functions for converting to/from bencoded strings
#Summary(pl.UTF-8):
Name:		perl-Convert-Bencode
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Convert/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	be0831c69fe581908d33bbebff0b5760
URL:		http://search.cpan.org/dist/Convert-Bencode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides two functions, bencode and bdecode, which encode
and decode bencoded strings respectivly.

bencode() expects to be passed a single value, which is either a
scalar, a arrary ref, or a hash ref, and it returns a scalar
containing the bencoded representation of the data structure it was
passed. If the value passed was a scalar, it returns either a bencoded
string, or a bencoded integer (floating points are not implemented,
and would be returned as a string rather than a integer). If the value
was a array ref, it returns a bencoded list, with all the values of
that array also bencoded recursivly. If the value was a hash ref, it
returns a bencoded dictionary (which for all intents and purposes can
be thought of as a synonym for hash) containing the recursivly
bencoded key and value pairs of the hash.

bdecode() expects to be passed a single scalar containing the bencoded
string to be decoded. Its return value will be either a hash ref, a
array ref, or a scalar, depending on whether the outer most element of
the bencoded string was a dictionary, list, or a string/integer
respectivly.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorlib}/Convert/*.pm
%{_mandir}/man3/*
