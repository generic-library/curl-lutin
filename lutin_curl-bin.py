#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os


def get_type():
	return "BINARY"

def get_desc():
	return "cURL binary"

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
	    'curl/src/slist_wc.c',
	    'curl/src/tool_binmode.c',
	    'curl/src/tool_bname.c',
	    'curl/src/tool_cb_dbg.c',
	    'curl/src/tool_cb_hdr.c',
	    'curl/src/tool_cb_prg.c',
	    'curl/src/tool_cb_rea.c',
	    'curl/src/tool_cb_see.c',
	    'curl/src/tool_cb_wrt.c',
	    'curl/src/tool_cfgable.c',
	    'curl/src/tool_convert.c',
	    'curl/src/tool_dirhie.c',
	    'curl/src/tool_doswin.c',
	    'curl/src/tool_easysrc.c',
	    'curl/src/tool_formparse.c',
	    'curl/src/tool_getparam.c',
	    'curl/src/tool_getpass.c',
	    'curl/src/tool_help.c',
	    'curl/src/tool_helpers.c',
	    'curl/src/tool_homedir.c',
	    #'curl/src/tool_hugehelp.c',
	    'generate/tool_hugehelp.c',
	    'curl/src/tool_libinfo.c',
	    'curl/src/tool_main.c',
	    'curl/src/tool_metalink.c',
	    'curl/src/tool_mfiles.c',
	    'curl/src/tool_msgs.c',
	    'curl/src/tool_operate.c',
	    'curl/src/tool_operhlp.c',
	    'curl/src/tool_panykey.c',
	    'curl/src/tool_paramhlp.c',
	    'curl/src/tool_parsecfg.c',
	    'curl/src/tool_strdup.c',
	    'curl/src/tool_setopt.c',
	    'curl/src/tool_sleep.c',
	    'curl/src/tool_urlglob.c',
	    'curl/src/tool_util.c',
	    'curl/src/tool_vms.c',
	    'curl/src/tool_writeenv.c',
	    'curl/src/tool_writeout.c',
	    'curl/src/tool_xattr.c',
	    'curl/lib/strtoofft.c',
	    'curl/lib/rawstr.c',
	    'curl/lib/nonblock.c',
	    'curl/lib/warnless.c',
	    ])
	my_module.compile_flags('c', [
	    '-DHAVE_CONFIG_H',
	    ])
	my_module.compile_version("c", 1989, gnu=True)
	my_module.add_module_depend('curl')
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "src"))
	# Bad lib implementation ...
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "lib"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "include"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "curl", "include", "curl"))
	my_module.add_path(os.path.join(tools.get_current_path(__file__), "generate"))
	# end bad
	return my_module

"""
',/home/heero/dev/perso/framework/curl-lutin/curl/src',,
-DHAVE_CONFIG_H
-I/home/heero/dev/perso/framework/curl-lutin/curl/include/curl
-I/home/heero/dev/perso/framework/curl-lutin/curl/include
-I/home/heero/dev/perso/framework/curl-lutin/curl/lib
-I/home/heero/dev/perso/framework/curl-lutin/curl/src

"""


