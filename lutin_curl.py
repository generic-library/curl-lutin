#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "LIBRARY"

def get_desc():
	return "cURL library"

def get_licence():
	return "MIT"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "haxx"

def get_maintainer():
	return ["Daniel Stenberg<daniel@haxx.se>"]

def get_version():
	return [7,48,0]

def create(target, module_name):
	my_module = module.Module(__file__, module_name, get_type())
	my_module.add_src_file([
	    'curl/lib/file.c',
	    'curl/lib/timeval.c',
	    'curl/lib/base64.c',
	    'curl/lib/hostip.c',
	    'curl/lib/progress.c',
	    'curl/lib/formdata.c',
	    'curl/lib/cookie.c',
	    'curl/lib/http.c',
	    'curl/lib/sendf.c',
	    'curl/lib/ftp.c',
	    'curl/lib/url.c',
	    'curl/lib/dict.c',
	    'curl/lib/if2ip.c',
	    'curl/lib/speedcheck.c',
	    'curl/lib/ldap.c',
	    'curl/lib/version.c',
	    'curl/lib/getenv.c',
	    'curl/lib/escape.c',
	    'curl/lib/mprintf.c',
	    'curl/lib/telnet.c',
	    'curl/lib/netrc.c',
	    'curl/lib/getinfo.c',
	    'curl/lib/transfer.c',
	    'curl/lib/strequal.c',
	    'curl/lib/easy.c',
	    'curl/lib/security.c',
	    'curl/lib/curl_fnmatch.c',
	    'curl/lib/fileinfo.c',
	    'curl/lib/ftplistparser.c',
	    'curl/lib/wildcard.c',
	    'curl/lib/krb5.c',
	    'curl/lib/memdebug.c',
	    'curl/lib/http_chunks.c',
	    'curl/lib/strtok.c',
	    'curl/lib/connect.c',
	    'curl/lib/llist.c',
	    'curl/lib/hash.c',
	    'curl/lib/multi.c',
	    'curl/lib/content_encoding.c',
	    'curl/lib/share.c',
	    'curl/lib/http_digest.c',
	    'curl/lib/md4.c',
	    'curl/lib/md5.c',
	    'curl/lib/http_negotiate.c',
	    'curl/lib/inet_pton.c',
	    'curl/lib/strtoofft.c',
	    'curl/lib/strerror.c',
	    'curl/lib/amigaos.c',
	    'curl/lib/hostasyn.c',
	    'curl/lib/hostip4.c',
	    'curl/lib/hostip6.c',
	    'curl/lib/hostsyn.c',
	    'curl/lib/inet_ntop.c',
	    'curl/lib/parsedate.c',
	    'curl/lib/select.c',
	    'curl/lib/tftp.c',
	    'curl/lib/splay.c',
	    'curl/lib/strdup.c',
	    'curl/lib/socks.c',
	    'curl/lib/ssh.c',
	    'curl/lib/rawstr.c',
	    'curl/lib/curl_addrinfo.c',
	    'curl/lib/socks_gssapi.c',
	    'curl/lib/socks_sspi.c',
	    'curl/lib/curl_sspi.c',
	    'curl/lib/slist.c',
	    'curl/lib/nonblock.c',
	    'curl/lib/curl_memrchr.c',
	    'curl/lib/imap.c',
	    'curl/lib/pop3.c',
	    'curl/lib/smtp.c',
	    'curl/lib/pingpong.c',
	    'curl/lib/rtsp.c',
	    'curl/lib/curl_threads.c',
	    'curl/lib/warnless.c',
	    'curl/lib/hmac.c',
	    'curl/lib/curl_rtmp.c',
	    'curl/lib/openldap.c',
	    'curl/lib/curl_gethostname.c',
	    'curl/lib/gopher.c',
	    'curl/lib/idn_win32.c',
	    'curl/lib/http_negotiate_sspi.c',
	    'curl/lib/http_proxy.c',
	    'curl/lib/non-ascii.c',
	    'curl/lib/asyn-ares.c',
	    'curl/lib/asyn-thread.c',
	    'curl/lib/curl_gssapi.c',
	    'curl/lib/curl_ntlm.c',
	    'curl/lib/curl_ntlm_wb.c',
	    'curl/lib/curl_ntlm_core.c',
	    'curl/lib/curl_ntlm_msgs.c',
	    'curl/lib/curl_sasl.c',
	    'curl/lib/curl_multibyte.c',
	    'curl/lib/hostcheck.c',
	    'curl/lib/conncache.c',
	    'curl/lib/pipeline.c',
	    'curl/lib/dotdot.c',
	    'curl/lib/x509asn1.c',
	    'curl/lib/http2.c',
	    'curl/lib/curl_sasl_sspi.c',
	    'curl/lib/smb.c',
	    'curl/lib/curl_sasl_gssapi.c',
	    'curl/lib/curl_endian.c',
	    'curl/lib/curl_des.c',
	    'curl/lib/vtls/openssl.c',
	    'curl/lib/vtls/gtls.c',
	    'curl/lib/vtls/vtls.c',
	    'curl/lib/vtls/nss.c',
	    'curl/lib/vtls/polarssl.c',
	    'curl/lib/vtls/polarssl_threadlock.c',
	    'curl/lib/vtls/axtls.c',
	    'curl/lib/vtls/cyassl.c',
	    'curl/lib/vtls/schannel.c',
	    'curl/lib/vtls/darwinssl.c',
	    'curl/lib/vtls/gskit.c',
	    'curl/lib/vtls/mbedtls.c',
	    ])
	my_module.add_flag('c', [
	    '-Dlibcurl_EXPORTS',
	    '-DBUILDING_LIBCURL',
	    '-DHAVE_CONFIG_H',
	    '-DCURL_DISABLE_LDAP',
	    ])
	my_module.compile_version("c", 1989, gnu=True)
	my_module.add_depend('z')
	my_module.add_depend('openssl')
	my_module.add_depend('ssh2')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "lib"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "include"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "include", "curl"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "generate"))
	my_module.add_header_file([
	    'curl/include/curl/mprintf.h',
	    'curl/include/curl/curlver.h',
	    'curl/include/curl/multi.h',
	    'curl/include/curl/curl.h',
	    'curl/include/curl/curlrules.h',
	    'curl/include/curl/typecheck-gcc.h',
	    'curl/include/curl/easy.h',
	    'curl/lib/curl_setup.h',
	    'generate/curlbuild.h',
	    ],
	    destination_path="curl")
	return my_module
