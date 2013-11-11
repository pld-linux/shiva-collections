Summary:	Collection of programs in Shiva language
Summary(pl.UTF-8):	Zbiór programów w języku Shiva
Name:		shiva-collections
Version:	1.4
Release:	1
License:	LGPL v2, MIT
Group:		X11/Applications/Graphics
Source0:	http://download.opengtl.org/%{name}-%{version}.tar.bz2
# Source0-md5:	101d266491e02e7fc8f9a056012e4d2a
URL:		http://www.opengtl.org/languages/shiva/
BuildRequires:	cmake >= 2.6
Requires:	OpenGTL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of programs in Shiva language.

Shiva is a programming language intented to transform an image by
applying a kernel-like transformation.

%description -l pl.UTF-8
Zbiór programów w języku Shiva.

Shiva to język programowania przeznaczony do przekształceń obrazów
poprzez nałożenie przekształcenia typu jądrowego.

%prep
%setup -q

%build
%cmake .

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/OpenGTL
%dir %{_datadir}/OpenGTL/shiva
%dir %{_datadir}/OpenGTL/shiva/kernels
%{_datadir}/OpenGTL/shiva/kernels/*.shiva
