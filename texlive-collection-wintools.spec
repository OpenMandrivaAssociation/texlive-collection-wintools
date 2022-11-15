Name:		texlive-collection-wintools
Version:	54074
Release:	1
Summary:	Windows-only support programs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/collection-wintools
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-wintools.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Utilities for Windows, since they are not readily available
there: chktex, unzip, wget, xpdf, and the dviout previewer.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
