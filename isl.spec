#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: 5424026
#
Name     : isl
Version  : 0.27
Release  : 1
URL      : https://libisl.sourceforge.io/isl-0.27.tar.gz
Source0  : https://libisl.sourceforge.io/isl-0.27.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: isl-lib = %{version}-%{release}
Requires: isl-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gmp-dev
BuildRequires : grep
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
isl is a thread-safe C library for manipulating sets and relations
of integer points bounded by affine constraints.  The descriptions of
the sets and relations may involve both parameters and existentially
quantified variables.  All computations are performed in exact integer
arithmetic using GMP.

%package dev
Summary: dev components for the isl package.
Group: Development
Requires: isl-lib = %{version}-%{release}
Provides: isl-devel = %{version}-%{release}
Requires: isl = %{version}-%{release}

%description dev
dev components for the isl package.


%package lib
Summary: lib components for the isl package.
Group: Libraries
Requires: isl-license = %{version}-%{release}

%description lib
lib components for the isl package.


%package license
Summary: license components for the isl package.
Group: Default

%description license
license components for the isl package.


%prep
%setup -q -n isl-0.27
cd %{_builddir}/isl-0.27

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1733424420
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1733424420
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/isl
cp %{_builddir}/isl-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/isl/45c2429b5881295597e96c81fc50f7b8a42e769f || :
export GOAMD64=v2
GOAMD64=v2
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/isl/aff.h
/usr/include/isl/aff_type.h
/usr/include/isl/arg.h
/usr/include/isl/ast.h
/usr/include/isl/ast_build.h
/usr/include/isl/ast_type.h
/usr/include/isl/constraint.h
/usr/include/isl/cpp.h
/usr/include/isl/ctx.h
/usr/include/isl/fixed_box.h
/usr/include/isl/flow.h
/usr/include/isl/hash.h
/usr/include/isl/hmap.h
/usr/include/isl/hmap_templ.c
/usr/include/isl/id.h
/usr/include/isl/id_to_ast_expr.h
/usr/include/isl/id_to_id.h
/usr/include/isl/id_to_pw_aff.h
/usr/include/isl/id_type.h
/usr/include/isl/ilp.h
/usr/include/isl/list.h
/usr/include/isl/local_space.h
/usr/include/isl/lp.h
/usr/include/isl/map.h
/usr/include/isl/map_to_basic_set.h
/usr/include/isl/map_type.h
/usr/include/isl/mat.h
/usr/include/isl/maybe.h
/usr/include/isl/maybe_ast_expr.h
/usr/include/isl/maybe_basic_set.h
/usr/include/isl/maybe_id.h
/usr/include/isl/maybe_pw_aff.h
/usr/include/isl/maybe_templ.h
/usr/include/isl/multi.h
/usr/include/isl/obj.h
/usr/include/isl/options.h
/usr/include/isl/point.h
/usr/include/isl/polynomial.h
/usr/include/isl/polynomial_type.h
/usr/include/isl/printer.h
/usr/include/isl/printer_type.h
/usr/include/isl/schedule.h
/usr/include/isl/schedule_node.h
/usr/include/isl/schedule_type.h
/usr/include/isl/set.h
/usr/include/isl/set_type.h
/usr/include/isl/space.h
/usr/include/isl/space_type.h
/usr/include/isl/stdint.h
/usr/include/isl/stream.h
/usr/include/isl/stride_info.h
/usr/include/isl/typed_cpp.h
/usr/include/isl/union_map.h
/usr/include/isl/union_map_type.h
/usr/include/isl/union_set.h
/usr/include/isl/union_set_type.h
/usr/include/isl/val.h
/usr/include/isl/val_gmp.h
/usr/include/isl/val_type.h
/usr/include/isl/vec.h
/usr/include/isl/version.h
/usr/include/isl/vertices.h
/usr/lib64/libisl.so
/usr/lib64/pkgconfig/isl.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libisl.so.23
/usr/lib64/libisl.so.23.4.0
/usr/lib64/libisl.so.23.4.0-gdb.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/isl/45c2429b5881295597e96c81fc50f7b8a42e769f
