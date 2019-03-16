{
  "win_delay_load_hook": "true",
  "targets": [
    {
      "target_name": "gstreamer-superficial",
      "sources": [ "gstreamer.cpp", "GLibHelpers.cpp", "GObjectWrap.cpp", "Pipeline.cpp" ],
	  "include_dirs": [
		"<!(node -e \"require('nan')\")"
	  ],
	  "conditions" : [
		["OS=='linux'", {
			"include_dirs": [
				'<!@(pkg-config gstreamer-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)'
			],
			"libraries": [
				'<!@(pkg-config gstreamer-1.0 --libs)',
				'<!@(pkg-config gstreamer-app-1.0 --libs)',
				'<!@(pkg-config gstreamer-video-1.0 --libs)'
			]
		}],
		["OS=='mac'", {
			"include_dirs": [
				'<!@(pkg-config gstreamer-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)',
				'<!@(pkg-config gstreamer-app-1.0 --cflags-only-I | sed s/-I//g)'
			],
			"libraries": [
				'<!@(pkg-config gstreamer-1.0 --libs)',
				'<!@(pkg-config gstreamer-app-1.0 --libs)',
				'<!@(pkg-config gstreamer-video-1.0 --libs)'
			]
		}],
		["OS=='win'", {
			"include_dirs": [
				"C:/gstreamer/1.0/x86/include/gstreamer-1.0",
				"C:/gstreamer/1.0/x86/include/glib-2.0",
				"C:/gstreamer/1.0/x86/lib/glib-2.0/include",
				"C:/gstreamer/1.0/x86/lib/libffi-3.99999/include"
			],
			"libraries": [
				"C:/gstreamer/1.0/x86/lib/gstreamer-1.0.lib",
				"C:/gstreamer/1.0/x86/lib/gstapp-1.0.lib",
				"C:/gstreamer/1.0/x86/lib/gstvideo-1.0.lib",
				"C:/gstreamer/1.0/x86/lib/gobject-2.0.lib",
				"C:/gstreamer/1.0/x86/lib/glib-2.0.lib"
			]
		}]
	  ]
    }
  ]
}
