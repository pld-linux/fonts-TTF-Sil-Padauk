Summary:	Free TrueType font for Myanmar script
Summary(pl.UTF-8):	Wolnodostępny font TrueType dla pisma birmańskiego
Name:		fonts-TTF-Sil-Padauk
Version:	2.6.1
Release:	1
License:	OFL, distributable
Group:		Fonts
# retrieved from: http://scripts.sil.org/cms/scripts/render_download.php?site_id=nrsi&format=file&media_id=MH_Padauk_tarball&filename=ttf-sil-padauk-2.6.1.tar.gz
Source0:	ttf-sil-padauk-2.6.1.tar.gz
# Source0-md5:	106e5ac364dfa2bb5329913bf26b1bd5
URL:		http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=Padauk
Requires(post,postun):	fontpostinst
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ttffontsdir	%{_fontsdir}/TTF

%description
Padauk is a fully capable Unicode 5.1 font supporting all the Myanmar
characters in the standard. Thus it provides support for minority
languages as well, in both local and Burmese rendering style.

#%%description -l pl.UTF-8
# TODO

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ttffontsdir}

install *.ttf $RPM_BUILD_ROOT%{ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc debian-src/copyright doc/*
%{ttffontsdir}/Padauk*.ttf
