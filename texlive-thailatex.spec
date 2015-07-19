# revision 27050
# category Package
# catalog-ctan /language/thai/thailatex
# catalog-date 2012-06-16 13:25:22 +0200
# catalog-license lppl
# catalog-version 0.5.0
Name:		texlive-thailatex
Version:	0.5.0
Release:	9
Summary:	Typeset Thai texts with standard LaTeX classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/thai/thailatex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thailatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thailatex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thailatex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
ThaiLaTeX enables typesetting Thai with standard LaTeX document
classes. It is designed to become a part of babel, and may be
used as such after a (small) patch to babel itself.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/thailatex/hyph-th-utf8.tex
%{_texmfdistdir}/tex/generic/thailatex/hyph-th.tex
%{_texmfdistdir}/tex/generic/thailatex/loadhyph-th.tex
%{_texmfdistdir}/tex/generic/thailatex/lthenc.def
%{_texmfdistdir}/tex/generic/thailatex/thai.ldf
%{_texmfdistdir}/tex/generic/thailatex/thswitch.sty
%{_texmfdistdir}/tex/generic/thailatex/tis620.def
%doc %{_texmfdistdir}/doc/latex/thailatex/README
%doc %{_texmfdistdir}/doc/latex/thailatex/examples/orchid.tex
%doc %{_texmfdistdir}/doc/latex/thailatex/examples/utf-example.tex
%doc %{_texmfdistdir}/doc/latex/thailatex/thai.pdf
#- source
%doc %{_texmfdistdir}/source/latex/thailatex/AUTHORS
%doc %{_texmfdistdir}/source/latex/thailatex/COPYING
%doc %{_texmfdistdir}/source/latex/thailatex/ChangeLog
%doc %{_texmfdistdir}/source/latex/thailatex/HISTORY
%doc %{_texmfdistdir}/source/latex/thailatex/INSTALL
%doc %{_texmfdistdir}/source/latex/thailatex/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/NEWS
%doc %{_texmfdistdir}/source/latex/thailatex/README
%doc %{_texmfdistdir}/source/latex/thailatex/README.hyphen
%doc %{_texmfdistdir}/source/latex/thailatex/TODO
%doc %{_texmfdistdir}/source/latex/thailatex/aclocal.m4
%doc %{_texmfdistdir}/source/latex/thailatex/babel/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/babel/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthenc.def
%doc %{_texmfdistdir}/source/latex/thailatex/babel/thai.dtx
%doc %{_texmfdistdir}/source/latex/thailatex/babel/thai.ins
%doc %{_texmfdistdir}/source/latex/thailatex/babel/thswitch.sty
%doc %{_texmfdistdir}/source/latex/thailatex/babel/tis620.def
%doc %{_texmfdistdir}/source/latex/thailatex/configure
%doc %{_texmfdistdir}/source/latex/thailatex/configure.in
%doc %{_texmfdistdir}/source/latex/thailatex/doc/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/doc/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/doc/orchid.tex
%doc %{_texmfdistdir}/source/latex/thailatex/doc/utf-example.tex
%doc %{_texmfdistdir}/source/latex/thailatex/emacs/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/emacs/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/emacs/thai-latex-setup.el
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/README
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/conv-utf8-hex.sed
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/diff-dicts.sh
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/hyph-th-utf8.tex.in
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/hyph-th.tex.in
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/loadhyph-th.tex
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-city.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-collection.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-common.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-country.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-district.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-geo.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-history.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-ict.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-lang-ethnic.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-proper.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-science.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-spell.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-std-compound.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/tdict-std.txt
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/test-hyphen.sh
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/thai-exc.pat
%doc %{_texmfdistdir}/source/latex/thailatex/hyphen/thai.tra
%doc %{_texmfdistdir}/source/latex/thailatex/install-sh
%doc %{_texmfdistdir}/source/latex/thailatex/missing
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/sync-babel
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/sync-thailatex.in
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/tlatex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.5.0-1
+ Revision: 812922
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4.7-1
+ Revision: 779703
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4.5-2
+ Revision: 756828
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4.5-1
+ Revision: 719725
- texlive-thailatex
- texlive-thailatex
- texlive-thailatex

