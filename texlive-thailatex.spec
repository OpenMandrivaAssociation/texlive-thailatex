# revision 21788
# category Package
# catalog-ctan /language/thai/thailatex
# catalog-date 2011-03-21 10:50:23 +0100
# catalog-license lppl
# catalog-version 0.4.5
Name:		texlive-thailatex
Version:	0.4.5
Release:	1
Summary:	Typeset Thai texts with standard LaTeX classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/thai/thailatex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thailatex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thailatex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
ThaiLaTeX enables typesetting Thai with standard LaTeX document
classes. It is designed to become a part of babel, and may be
used as such after a (small) patch to babel itself.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/thailatex/garuda.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/garuda_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/garuda_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/garuda_o.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/kinnari.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/kinnari_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/kinnari_bi.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/kinnari_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/kinnari_i.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/kinnari_o.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/loma.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/loma_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/loma_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/loma_o.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/norasi.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/norasi_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/norasi_bi.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/norasi_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/norasi_i.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/norasi_o.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/purisa.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/purisa_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/purisa_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/purisa_o.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/sawasdee.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/sawasdee_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/sawasdee_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/sawasdee_o.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/thai-dummy.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/ttype.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/ttype_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/ttype_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/ttype_o.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/ttypist.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/ttypist_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/ttypist_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/ttypist_o.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/umpush.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/umpush_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/umpush_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/umpush_o.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/waree.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/waree_b.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/waree_bo.afm
%{_texmfdistdir}/fonts/afm/public/thailatex/waree_o.afm
%{_texmfdistdir}/fonts/type1/public/thailatex/garuda.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/garuda_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/garuda_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/garuda_o.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/kinnari.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/kinnari_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/kinnari_bi.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/kinnari_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/kinnari_i.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/kinnari_o.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/loma.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/loma_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/loma_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/loma_o.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/norasi.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/norasi_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/norasi_bi.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/norasi_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/norasi_i.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/norasi_o.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/purisa.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/purisa_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/purisa_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/purisa_o.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/sawasdee.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/sawasdee_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/sawasdee_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/sawasdee_o.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/ttype.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/ttype_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/ttype_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/ttype_o.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/ttypist.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/ttypist_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/ttypist_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/ttypist_o.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/umpush.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/umpush_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/umpush_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/umpush_o.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/waree.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/waree_b.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/waree_bo.pfb
%{_texmfdistdir}/fonts/type1/public/thailatex/waree_o.pfb
#- source
%doc %{_texmfdistdir}/source/latex/thailatex/AUTHORS
%doc %{_texmfdistdir}/source/latex/thailatex/COPYING
%doc %{_texmfdistdir}/source/latex/thailatex/COPYING.fonts
%doc %{_texmfdistdir}/source/latex/thailatex/ChangeLog
%doc %{_texmfdistdir}/source/latex/thailatex/HISTORY
%doc %{_texmfdistdir}/source/latex/thailatex/INSTALL
%doc %{_texmfdistdir}/source/latex/thailatex/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/NEWS
%doc %{_texmfdistdir}/source/latex/thailatex/README
%doc %{_texmfdistdir}/source/latex/thailatex/TODO
%doc %{_texmfdistdir}/source/latex/thailatex/aclocal.m4
%doc %{_texmfdistdir}/source/latex/thailatex/babel/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/babel/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthenc.def
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthgaruda.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthkinnari.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthloma.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthnorasi.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthpurisa.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthsawasdee.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthttype.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthttypist.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthumpush.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/lthwaree.fd
%doc %{_texmfdistdir}/source/latex/thailatex/babel/thai.dtx
%doc %{_texmfdistdir}/source/latex/thailatex/babel/thai.ins
%doc %{_texmfdistdir}/source/latex/thailatex/babel/thai.sty
%doc %{_texmfdistdir}/source/latex/thailatex/babel/thswitch.sty
%doc %{_texmfdistdir}/source/latex/thailatex/babel/tis620.def
%doc %{_texmfdistdir}/source/latex/thailatex/configure
%doc %{_texmfdistdir}/source/latex/thailatex/configure.in
%doc %{_texmfdistdir}/source/latex/thailatex/doc/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/doc/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/doc/orchid.tex
%doc %{_texmfdistdir}/source/latex/thailatex/doc/test-orchid.sh
%doc %{_texmfdistdir}/source/latex/thailatex/doc/test-teststd.sh
%doc %{_texmfdistdir}/source/latex/thailatex/doc/test-utf.sh
%doc %{_texmfdistdir}/source/latex/thailatex/doc/teststd.tex
%doc %{_texmfdistdir}/source/latex/thailatex/doc/thai.pdf
%doc %{_texmfdistdir}/source/latex/thailatex/doc/utf-example.tex
%doc %{_texmfdistdir}/source/latex/thailatex/emacs/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/emacs/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/emacs/thai-latex-setup.el
%doc %{_texmfdistdir}/source/latex/thailatex/fonts/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/fonts/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/fonts/lthuni.enc
%doc %{_texmfdistdir}/source/latex/thailatex/fonts/thailigs.enc
%doc %{_texmfdistdir}/source/latex/thailatex/install-sh
%doc %{_texmfdistdir}/source/latex/thailatex/missing
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/Makefile.am
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/Makefile.in
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/sync-babel
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/sync-thailatex.in
%doc %{_texmfdistdir}/source/latex/thailatex/scripts/tlatex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
