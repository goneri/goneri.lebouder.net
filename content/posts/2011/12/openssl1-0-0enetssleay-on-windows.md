+++
title = "OpenSSL1.0.0e+Net::SSLeay on Windows"
date = 2011-12-03T01:24:37+00:00
[taxonomies]
tags = ["tips", "security"]
+++
I managed to get Net::SSLeay to work with the latest OpenSSL release. Here are just some notes for myself.

OpenSSL test-suite build will fail but the .a and the openssl.exe files are ok.
```
; LIBPATH=`echo $LIBPATH | sed -e 's/ /:/g'`; LD\_LIBRARY\_PATH=$LIBPATH:$LD\_LIBRARY\_PATH ${LDCMD} ${LDFLAGS} -o ${APPNAME:=ideatest.exe} ideatest.o ${LIBDEPS} )
make[2]: Leaving directory `/cygdrive/c/strawberry/openssl-1.0.0e/test'
gcc -I.. -I../include -DOPENSSL\_THREADS -D\_MT -DDSO\_WIN32 -DL\_ENDIAN -DWIN32\_LEAN\_AND\_MEAN -fomit-frame-pointer -O3 -march=i486 -Wall -DOPENSSL\_BN\_ASM\_PART\_WORDS -DOPENSSL\_IA32\_SSE2 -DOPENSSL\_BN\_ASM\_MONT -DSHA1\_ASM -DSHA256\_ASM -DSHA512\_ASM -DMD5\_ASM -DRMD160\_ASM -DAES\_ASM -DWHIRLPOOL\_ASM -c -o md2test.o md2test.c
md2test.c:1: error: expected identifier or '(' before '!' token
md2test.c:1: error: stray '\\377' in program
md2test.c:1: error: stray '\\376' in program
md2test.c:1:14: warning: null character(s) ignored
md2test.c:1:16: warning: null character(s) ignored
md2test.c:1:18: warning: null character(s) ignored
md2test.c:1:20: warning: null character(s) ignored
md2test.c:1:22: warning: null character(s) ignored
md2test.c:1:24: warning: null character(s) ignored
md2test.c:1:26: warning: null character(s) ignored
md2test.c:1:28: warning: null character(s) ignored
md2test.c:1:30: warning: null character(s) ignored
md2test.c:1:32: warning: null character(s) ignored
md2test.c:1:34: warning: null character(s) ignored
: recipe for target `md2test.o' failed
make[1]: \*\*\* [md2test.o] Error 1
make[1]: Leaving directory `/cygdrive/c/strawberry/openssl-1.0.0e/test'
Makefile:255: recipe for target `build\_tests' failed
make: \*\*\* [build\_tests] Error 1 Administrator@ordi-de-gon▒ri /cygdrive/c/strawberry/openssl-1.0.0e
```

The openssl.exe binary is in apps/ on Windows, not bin. Net::SSLeay's Makefile.PL file fails to find the OpenSSL distribution because of that.

```
(...)
c:\\strawberry\\openssl-1.0.0e\\libcrypto.a(e\_capi.o):e\_capi.c:(.text+0x251a): undefined reference to `\_imp\_\_CertOpenStore@20'
c:\\strawberry\\openssl-1.0.0e\\libcrypto.a(e\_capi.o):e\_capi.c:(.text+0x255f): undefined reference to `imp\_\_CertFreeCertificateContext@4'
c:\\strawberry\\openssl-1.0.0e\\libcrypto.a(e\_capi.o):e\_capi.c:(.text+0x2576): undefined reference to `\_imp\_\_CertCloseStore@8'
c:\\strawberry\\openssl-1.0.0e\\libcrypto.a(e\_capi.o):e\_capi.c:(.text+0x25d5): undefined reference to `\_imp\_\_CertEnumCertificatesInStore@8'
c:\\strawberry\\openssl-1.0.0e\\libcrypto.a(e\_capi.o):e\_capi.c:(.text+0x2e1a): undefined reference to `\_imp\_\_CertOpenStore@20'
c:\\strawberry\\openssl-1.0.0e\\libcrypto.a(e\_capi.o):e\_capi.c:(.text+0x2e4d): undefined reference to `\_imp\_\_CertEnumCertificatesInStore@8'
c:\\strawberry\\openssl-1.0.0e\\libcrypto.a(e\_capi.o):e\_capi.c:(.text+0x2f28): undefined reference to `\_imp\_\_CertDuplicateCertificateContext@4'
c:\\strawberry\\openssl-1.0.0e\\libcrypto.a(e\_capi.o):e\_capi.c:(.text+0x2fb1): undefined reference to `\_imp\_\_CertCloseStore@8'
c:\\strawberry\\openssl-1.0.0e\\libcrypto.a(e\_capi.o):e\_capi.c:(.text+0x30e6): undefined reference to `\_imp\_\_CertFreeCertificateContext@4'
collect2: ld returned 1 exit status
dmake: Error code 129, while making 'blib\\arch\\auto\\Net\\SSLeay\\SSLeay.dll'
```

The patch to apply to get Net::SSLeay to build.
```diff
--- Net-SSLeay-1.42.orig/inc/Module/Install/PRIVATE/Net/SSLeay.pm 2011-10-03 08:23:34.000000000 +0200
+++ Net-SSLeay-1.42/inc/Module/Install/PRIVATE/Net/SSLeay.pm 2011-12-03 02:22:28.286660290 +0100
@@ -90,7 +90,7 @@ EOM # libeay32 and ssleay32. # This construction will not complain as long as it find at least one # libssl32.a is made by openssl onWin21 with the ms/minw32.bat builder
- push @{ $opts-\>{lib\_links} }, qw( libeay32MD ssleay32MD libeay32 ssleay32 libssl32);
+ push @{ $opts-\>{lib\_links} }, qw( libssl libcrypto Crypt32 ); } else { $opts-\>{optimize} = '-O2 -g'; push @{ $opts-\>{lib\_links} },
@@ -172,9 +172,10 @@ sub find\_openssl\_exec { my ($self, $prefix) = @\_; my $exe\_path;
- for my $subdir (qw( bin sbin out32dll )) {
+ for my $subdir (qw( apps bin sbin out32dll )) { my $path = File::Spec-\>catfile($prefix, $subdir, "openssl$Config{\_exe}");
- if ( -x $path ) {
+
+ if ( -e $path ) { return $path; } }
```
