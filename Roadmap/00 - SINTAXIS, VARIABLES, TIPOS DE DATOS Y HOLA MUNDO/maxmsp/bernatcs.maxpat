{
	"boxes" : [ 		{
			"box" : 			{
				"maxclass" : "newobj",
				"text" : "print @popup 1",
				"numinlets" : 1,
				"fontname" : "Arial",
				"patching_rect" : [ 40.0, 567.0, 102.0, 23.0 ],
				"numoutlets" : 0,
				"id" : "obj-19",
				"fontsize" : 13.0
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "message",
				"text" : "¡Hola, MaxMSP!",
				"numinlets" : 2,
				"patching_rect" : [ 40.0, 530.0, 96.0, 22.0 ],
				"numoutlets" : 1,
				"outlettype" : [ "" ],
				"id" : "obj-30"
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "kslider",
				"numinlets" : 2,
				"patching_rect" : [ 40.0, 408.0, 336.0, 53.0 ],
				"numoutlets" : 2,
				"outlettype" : [ "int", "int" ],
				"id" : "obj-26",
				"parameter_enable" : 0
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "button",
				"numinlets" : 1,
				"patching_rect" : [ 252.0, 368.0, 24.0, 24.0 ],
				"numoutlets" : 1,
				"outlettype" : [ "bang" ],
				"id" : "obj-18",
				"parameter_enable" : 0
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "toggle",
				"numinlets" : 1,
				"patching_rect" : [ 218.0, 368.0, 24.0, 24.0 ],
				"numoutlets" : 1,
				"outlettype" : [ "int" ],
				"id" : "obj-16",
				"parameter_enable" : 0
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "message",
				"numinlets" : 2,
				"patching_rect" : [ 156.5, 369.0, 50.0, 22.0 ],
				"numoutlets" : 1,
				"outlettype" : [ "" ],
				"id" : "obj-14"
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "flonum",
				"numinlets" : 1,
				"patching_rect" : [ 99.0, 369.0, 50.0, 22.0 ],
				"numoutlets" : 2,
				"format" : 6,
				"outlettype" : [ "", "bang" ],
				"id" : "obj-12",
				"parameter_enable" : 0
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "number",
				"numinlets" : 1,
				"patching_rect" : [ 40.0, 369.0, 50.0, 22.0 ],
				"numoutlets" : 2,
				"outlettype" : [ "", "bang" ],
				"id" : "obj-10",
				"parameter_enable" : 0
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "comment",
				"text" : "Estos son los objetos habituales:",
				"numinlets" : 1,
				"patching_rect" : [ 40.0, 327.0, 283.0, 20.0 ],
				"numoutlets" : 0,
				"id" : "obj-8"
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "message",
				"text" : "No existen las Variables en Max. En cambio puedes utilizar diferentes elementos [como este] para asignarle valores cambiantes",
				"numinlets" : 2,
				"patching_rect" : [ 40.0, 210.0, 689.0, 22.0 ],
				"numoutlets" : 1,
				"outlettype" : [ "" ],
				"id" : "obj-6"
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "comment",
				"text" : "Esto es un comentario y ya está",
				"presentation_linecount" : 2,
				"numinlets" : 1,
				"patching_rect" : [ 40.0, 136.0, 304.0, 20.0 ],
				"numoutlets" : 0,
				"id" : "obj-3"
			}

		}
, 		{
			"box" : 			{
				"maxclass" : "comment",
				"text" : "https://cycling74.com/",
				"numinlets" : 1,
				"patching_rect" : [ 40.0, 81.0, 150.0, 20.0 ],
				"numoutlets" : 0,
				"id" : "obj-2"
			}

		}
 ],
	"lines" : [ 		{
			"patchline" : 			{
				"source" : [ "obj-30", 0 ],
				"destination" : [ "obj-19", 0 ]
			}

		}
 ],
	"appversion" : 	{
		"major" : 8,
		"minor" : 6,
		"revision" : 2,
		"architecture" : "x64",
		"modernui" : 1
	}
,
	"classnamespace" : "box"
}
