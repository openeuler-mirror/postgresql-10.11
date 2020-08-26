Name:           postgresql
Version:        10.11
Release:        1%{?dist}
Summary:        internet adapter software

License:        GPL	
URL:            https://www.postgresql.org/ftp/source/v10.11/
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  make
BuildRequires: gcc
BuildRequires: perl(ExtUtils::MakeMaker) glibc-devel bison flex gawk
BuildRequires: perl(ExtUtils::Embed), perl-devel
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: perl-generators
%endif
BuildRequires: readline-devel zlib-devel
BuildRequires: systemd systemd-devel util-linux
BuildRequires: multilib-rpm-config

# postgresql-setup build requires
BuildRequires: m4 elinks docbook-utils help2man




# main package requires -libs subpackage


# https://bugzilla.redhat.com/1464368
%global __provides_exclude_from %{_libdir}/pgsql

%description
internet adapter software to OpenEuler+KunPeng 

%prep
%autosetup


%build
%configure
%make_build 


%install
%make_install 


%files
/usr/include/libpq-events.h
/usr/include/postgres_ext.h
/usr/include/sqlca.h
/usr/include/pg_config_ext.h
/usr/include/ecpg_config.h
/usr/include/pg_config_os.h
/usr/include/pgtypes_timestamp.h
/usr/include/libpq
/usr/include/libpq/libpq-fs.h
/usr/include/libpq-fe.h
/usr/include/pgtypes_date.h
/usr/include/ecpg_informix.h
/usr/include/pgtypes.h
/usr/include/ecpgtype.h
/usr/include/pgtypes_error.h
/usr/include/postgresql/*
/usr/include/pgtypes_numeric.h
/usr/include/sqlda-compat.h
/usr/include/ecpglib.h
/usr/include/pg_config_manual.h
/usr/include/sqlda-native.h
/usr/include/pg_config.h
/usr/include/pgtypes_interval.h
/usr/include/sql3types.h
/usr/include/sqlda.h
/usr/include/ecpgerrno.h
/usr/share/postgresql/*
/usr/lib64/libecpg.so.6
/usr/lib64/libecpg_compat.so.3.10
/usr/lib64/libpgtypes.so.3.10
/usr/lib64/pkgconfig
/usr/lib64/pkgconfig/libpq.pc
/usr/lib64/pkgconfig/libpgtypes.pc
/usr/lib64/pkgconfig/libecpg_compat.pc
/usr/lib64/pkgconfig/libecpg.pc
/usr/lib64/libecpg.so.6.10
/usr/lib64/libpq.so.5
/usr/lib64/libpgcommon.a
/usr/lib64/libpq.a
/usr/lib64/libecpg_compat.so.3
/usr/lib64/libpgtypes.a
/usr/lib64/libpq.so.5.10
/usr/lib64/libecpg.so
/usr/lib64/libpgtypes.so
/usr/lib64/libpq.so
/usr/lib64/libpgport.a
/usr/lib64/postgresql/*
/usr/lib64/libecpg_compat.a
/usr/lib64/libecpg_compat.so
/usr/lib64/libpgtypes.so.3
/usr/lib64/libpgfeutils.a
/usr/lib64/libecpg.a
/usr/bin/ecpg
/usr/bin/pg_rewind
/usr/bin/pg_test_fsync
/usr/bin/postmaster
/usr/bin/pg_restore
/usr/bin/reindexdb
/usr/bin/initdb
/usr/bin/pg_config
/usr/bin/pg_controldata
/usr/bin/pg_ctl
/usr/bin/dropuser
/usr/bin/pg_dump
/usr/bin/pg_upgrade
/usr/bin/psql
/usr/bin/pg_dumpall
/usr/bin/pg_basebackup
/usr/bin/pg_test_timing
/usr/bin/clusterdb
/usr/bin/postgres
/usr/bin/pgbench
/usr/bin/pg_receivewal
/usr/bin/createdb
/usr/bin/vacuumdb
/usr/bin/pg_recvlogical
/usr/bin/pg_waldump
/usr/bin/pg_isready
/usr/bin/dropdb
/usr/bin/pg_resetwal
/usr/bin/createuser
/usr/bin/pg_archivecleanup



%changelog
* Mon Jul 20 2020 yangxianzhao
- 
