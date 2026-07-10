%global tl_name collection-wintools
%global tl_revision 65952

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Windows-only support programs
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-wintools
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-wintools.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(dviout.windows)
Requires:	texlive(wintools.windows)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Utilities for Windows, since they are not readily available there:
chktex, unzip, wget, xpdf, and the dviout previewer.

