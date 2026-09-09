model_tree_start yes
pro_unit_sys mmks
use_major_units yes
www_tree_location in
pro_unit_mass unit_kilogram
display shade
add_weld_mp yes
allow_anatomic_features yes
allow_move_attach_in_dtl_move yes
allow_package_children all
ang_dim_in_screen yes
ang_units ang_deg
angular_tol 0 1
auto_associate_dimensions yes
auto_regen_views yes
bell no
bitmap_size 300
chamfer_45deg_dim_text iso/din
company_name ZIMA-Engineering
copy_dxf_dim_pict no
dazix_default_placement_unit mm
dim_fraction_format std
display_axes no
display_axis_tags no
file_open_default_folder working_directory
format_setup_file /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/config/drawing.dtl
linear_tol 3 0.001
make_parameters_from_fmt_tables yes
pro_symbol_dir /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/symboly
pro_unit_length unit_mm
show_dim_sign no
trail_dir /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/trail
pro_format_dir /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/format
start_model_dir /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/temp
autodrill_udf_dir /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/udf
tol_mode nominal
mass_property_calculate automatic
pro_colormap_path ./text
display_coord_sys no
display_planes no

mdl_tree_cfg_file /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/config/tree.cfg
template_solidpart /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/temp/mmks_part_solid.prt.7
template_designasm /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/temp/mmks_asm_design.asm.5
template_drawing /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/format/a4.frm.33
mapkey $F6 @MAPKEY_LABELclose;~ Select `main_dlg_cur` `MenuBar1`1  `Windows`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `Windows.psh_win_close`;
mapkey $F8 @MAPKEY_LABELprint;~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;~ Activate `main_dlg_cur` `File.psh_print`;\
mapkey(continued) ~ Activate `print` `ToFile`1 ;~ Activate `print` `ToPrinter`0 ;\
mapkey(continued) ~ Select `print` `CascadeButton1`;~ Close `print` `CascadeButton1`;\
mapkey(continued) ~ Activate `print` `Generic Postscript`;~ Activate `print` `ToFile`1 ;\
mapkey(continued) ~ Activate `print` `ToPrinter`0 ;~ Activate `print` `OK`;\
mapkey(continued) ~ Activate `Print_file` `OK`;~ FocusIn `UI Message Dialog` `yes`;\
mapkey(continued) ~ Activate `UI Message Dialog` `yes`;

mapkey $F7 @MAPKEY_LABELiges;~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Select `file_saveas` `ph_list.Filelist`1  `export`;\
mapkey(continued) ~ Activate `file_saveas` `ph_list.Filelist`1  `export`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_134`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;\
mapkey(continued) ~ Move `intf_export` `intf_export`2 23.212677 15.833194 ;\
mapkey(continued) ~ Activate `intf_export` `solids`1 ;~ Activate `intf_export` `OkPushBtn`;
mapkey $F7 @MAPKEY_LABELiges;~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_134`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;\
mapkey(continued) ~ Move `intf_export` `intf_export`2 29.984987 14.245204 ;\
mapkey(continued) ~ Activate `intf_export` `solids`1 ;~ Activate `intf_export` `OkPushBtn`;\
mapkey(continued) ~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_539`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;~ Activate `intf_export` `shells`0 ;\
mapkey(continued) ~ Activate `intf_export` `OkPushBtn`;\
mapkey(continued) ~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_549`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;~ FocusOut `export_slice` `ChordHeightPanel`;\
mapkey(continued) ~ Select `export_slice` `BinaryAsciiRadioGroup`1  `ASCII`;\
mapkey(continued) ~ Activate `export_slice` `OK`;
mapkey $F5 @MAPKEY_LABELsave;\
mapkey(continued) ~ Activate `main_dlg_cur` `ProCmdModelSave.file`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;
mapkey $F12 @MAPKEY_LABELPARAMETRES;\
mapkey(continued) ~ Select `main_dlg_cur` `PHTLeft.AssyTree`1  `node0`;\
mapkey(continued) ~ RButtonArm `main_dlg_cur` `PHTLeft.AssyTree` `node0`;\
mapkey(continued) ~ PopupOver `main_dlg_cur` `ActionMenu`1  `PHTLeft.AssyTree`;\
mapkey(continued) ~ Open `main_dlg_cur` `ActionMenu`;~ Close `main_dlg_cur` `ActionMenu`;\
mapkey(continued) ~ Activate `main_dlg_cur` `EditParameters`;\
mapkey(continued) ~ FocusIn `relation_dlg` `ParamsPHLay.ParTable`;\
mapkey(continued) ~ Move `relation_dlg` `relation_dlg`2 12.517098 7.496247 ;\
mapkey(continued) ~ Activate `relation_dlg` `ParamsPHLay.TBAddParam`;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5111918 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4259937 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5898362 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4522085 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5636214 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`524296 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`524296 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`524296 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`524296 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`524296 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5111886 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4259905 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5898330 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4522053 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5636182 ;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Open `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Close `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable_INPUT`1  `string`;\
mapkey(continued) ~ Activate `relation_dlg` `ParamsPHLay.TBAddParam`;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4456516 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4259905 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5505108 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5570645 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5046349 ;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Open `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Close `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable_INPUT`1  `string`;\
mapkey(continued) ~ Activate `relation_dlg` `ParamsPHLay.TBAddParam`;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5111886 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5177423 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5374034 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5046349 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4259905 ;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Open `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Close `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable_INPUT`1  `string`;\
mapkey(continued) ~ Activate `relation_dlg` `ParamsPHLay.TBAddParam`;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5242960 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5177423 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4980812 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5177423 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5505108 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5177423 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5636182 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4259905 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5374034 ;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Open `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Close `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable_INPUT`1  `string`;\
mapkey(continued) ~ Activate `relation_dlg` `ParamsPHLay.TBAddParam`;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5046349 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4259905 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5505108 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4522053 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5374034 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4784201 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4259905 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4980812 ;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Open `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Close `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable_INPUT`1  `string`;\
mapkey(continued) ~ Activate `relation_dlg` `ParamsPHLay.TBAddParam`;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5046349 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5111886 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5177423 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5898330 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5439571 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5505108 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5636182 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4784201 ;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Open `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Close `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable_INPUT`1  `string`;\
mapkey(continued) ~ Activate `relation_dlg` `ParamsPHLay.TBAddParam`;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4915275 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5374034 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4522053 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5439571 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4980812 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4784201 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4980812 ;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Open `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Close `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable_INPUT`1  `string`;\
mapkey(continued) ~ Activate `relation_dlg` `ParamsPHLay.TBAddParam`;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5439571 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4390979 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4718664 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5636182 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4259905 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4980812 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4784201 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4980812 ;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Open `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Close `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable_INPUT`1  `string`;\
mapkey(continued) ~ Activate `relation_dlg` `ParamsPHLay.TBAddParam`;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5636182 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4522053 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5374034 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`5898330 ;\
mapkey(continued) ~ Key `relation_dlg` `ParamsPHLay.ParTable`4522053 ;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `new_added_row` `type`;\
mapkey(continued) ~ Open `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Close `relation_dlg` `ParamsPHLay.ParTable_INPUT`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable_INPUT`1  `string`;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `rowVERZE` `value`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `rowVERZE` `value`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `rowVERZE` `value`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `0`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `00`;\
mapkey(continued) ~ Update `relation_dlg` `ParamsPHLay.ParTable_INPUT` `00`;\
mapkey(continued) ~ FocusIn `relation_dlg` `ParamsPHLay.ParTable`;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `rowKRESLIL` `value`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `rowKRESLIL` `value`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `rowKRESLIL` `value`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `i`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `iN`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `iNG`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `iNG.`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `iNG`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `iN`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `i`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` ``;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `I`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `IN`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING.`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. `;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. V`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VL`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLA`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLAD`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADI`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADIM`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADIMI`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADIMIR`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADIMIR `;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADIMIR Z`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADIMIR ZI`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADIMIR ZIM`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADIMIR ZIMA`;\
mapkey(continued) ~ Update `relation_dlg` `ParamsPHLay.ParTable_INPUT` `ING. VLADIMIR ZIMA`;\
mapkey(continued) ~ FocusIn `relation_dlg` `ParamsPHLay.ParTable`;\
mapkey(continued) ~ Arm `relation_dlg` `ParamsPHLay.ParTable`2  `rowMNOZSTVI` `value`;\
mapkey(continued) ~ Disarm `relation_dlg` `ParamsPHLay.ParTable`2  `rowMNOZSTVI` `value`;\
mapkey(continued) ~ Select `relation_dlg` `ParamsPHLay.ParTable`2  `rowMNOZSTVI` `value`;\
mapkey(continued) ~ Input `relation_dlg` `ParamsPHLay.ParTable_INPUT` `1`;\
mapkey(continued) ~ Update `relation_dlg` `ParamsPHLay.ParTable_INPUT` `1`;\
mapkey(continued) ~ Activate `relation_dlg` `PB_OK`;\
mapkey(continued) ~ Select `main_dlg_cur` `MenuBar1`1  `Edit`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;~ Activate `main_dlg_cur` `Edit.pshSetup`;\
mapkey(continued) #MATERIAL;\
mapkey(continued) ~ Select `material_finder` `MtrlFFileListPHLay.Filelist`1  `steel.mtl`;\
mapkey(continued) ~ Activate `material_finder` `MtrlFFromLibToModelPush`;\
mapkey(continued) ~ Activate `material_finder` `MtrlFOkPush`;#DONE;\
mapkey(continued) ~ Activate `main_dlg_cur` `ProCmdRegenPart.edit_t`;\
mapkey(continued) ~ Select `main_dlg_cur` `MenuBar1`1  `Utilities`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `Utilities.psh_rels`;\
mapkey(continued) ~ FocusIn `relation_dlg` `RelText`;\
mapkey(continued) ~ Update `relation_dlg` `RelText` `hmotnost=ceil(mp_mass(\"\"), 2)`;\
mapkey(continued) ~ Activate `relation_dlg` `PB_OK`;
mapkey $F9 @MAPKEY_LABELstep-iges;\
mapkey(continued) ~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_134`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;\
mapkey(continued) ~ Move `intf_export` `intf_export`2 24.053378 12.750626 ;\
mapkey(continued) ~ Activate `intf_export` `solids`1 ;~ Activate `intf_export` `OkPushBtn`;\
mapkey(continued) ~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_539`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;~ Activate `intf_export` `shells`0 ;\
mapkey(continued) ~ Activate `intf_export` `OkPushBtn`;
mapkey $F7 @MAPKEY_LABELSTEP;~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Select `file_saveas` `ph_list.Filelist`1  `export`;\
mapkey(continued) ~ Activate `file_saveas` `ph_list.Filelist`1  `export`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_539`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;~ Activate `UI Message Dialog` `ok`;\
mapkey(continued) ~ Activate `intf_export` `solids`0 ;~ Activate `intf_export` `solids`1 ;\
mapkey(continued) ~ Activate `intf_export` `shells`0 ;~ Activate `intf_export` `OkPushBtn`;









drawing_setup_file /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/config/drawing.dtl
mapkey $F1 @MAPKEY_LABELJPEG;~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_566`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;~ Activate `shd_img_param` `OK`;
mapkey $F2 @MAPKEY_LABELDXF;~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Select `file_saveas` `ph_list.Filelist`1  `export`;\
mapkey(continued) ~ Activate `file_saveas` `ph_list.Filelist`1  `export`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_137`;\
mapkey(continued) ~ Update `file_saveas` `Inputname` `r360-0102-0101`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;~ Activate `export_2d_dlg` `OK_Button`;\
mapkey(continued) ~ Activate `UI Message Dialog` `ok`;
mapkey ; ~ Select `main_dlg_cur` `MenuBar1`1  `Insert`;\
mapkey(continued) ~ Select `main_dlg_cur` `Insert.cb_cosmetic`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Close `main_dlg_cur` `Insert.cb_cosmetic`;\
mapkey(continued) ~ Activate `main_dlg_cur` `pshThread`;
radial_hole_linear_dim yes
mapkey $F1 @MAPKEY_LABELthumbnails;\
mapkey(continued) ~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Select `main_dlg_cur` `File.cb_file_erase`;\
mapkey(continued) ~ Close `main_dlg_cur` `File.cb_file_erase`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Select `file_saveas` `ph_list.Filelist`1  `0000-index`;\
mapkey(continued) ~ Activate `file_saveas` `ph_list.Filelist`1  `0000-index`;\
mapkey(continued) ~ Select `file_saveas` `ph_list.Filelist`1  `thumbnails`;\
mapkey(continued) ~ Activate `file_saveas` `ph_list.Filelist`1  `thumbnails`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_566`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;~ FocusIn `UI Message Dialog` `ok`;\
mapkey(continued) ~ Activate `UI Message Dialog` `ok`;~ Activate `shd_img_param` `OK`;
mapkey $F7 @MAPKEY_LABELdwg;~ Activate `main_dlg_cur` `ProCmdViewRefit.view`;\
mapkey(continued) ~ Select `main_dlg_cur` `MenuBar1`1  `File`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `File.psh_save_as`;\
mapkey(continued) ~ Select `file_saveas` `ph_list.Filelist`1  `export`;\
mapkey(continued) ~ Activate `file_saveas` `ph_list.Filelist`1  `export`;\
mapkey(continued) ~ Open `file_saveas` `type_option`;~ Close `file_saveas` `type_option`;\
mapkey(continued) ~ Select `file_saveas` `type_option`1  `db_560`;\
mapkey(continued) ~ Activate `file_saveas` `OK`;~ Activate `export_2d_dlg` `OK_Button`;
mapkey o ~ Select `main_dlg_cur` `MenuBar1`1  `Utilities`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `Utilities.psh_util_pref`;\
mapkey(continued) ~ FocusOut `preferences` `InputOpt`;~ Activate `preferences` `Open`;\
mapkey(continued) ~ Select `file_open` `Ph_list.Filelist`1  `config.pro`;\
mapkey(continued) ~ Activate `file_open` `Ph_list.Filelist`1  `config.pro`;\
mapkey(continued) ~ Activate `preferences` `ok`;
mapkey o ~ Select `main_dlg_cur` `MenuBar1`1  `Utilities`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Activate `main_dlg_cur` `Utilities.psh_util_pref`;\
mapkey(continued) ~ FocusOut `preferences` `InputOpt`;~ Activate `preferences` `Open`;\
mapkey(continued) ~ Select `file_open` `Ph_list.Filelist`1  `config.pro`;\
mapkey(continued) ~ Activate `file_open` `Open`;~ Activate `preferences` `ok`;
mapkey o ~ Select `main_dlg_cur` `MenuBar1`1  `Utilities`;\
mapkey(continued) ~ Close `main_dlg_cur` `MenuBar1`;\
mapkey(continued) ~ Timer `UI Desktop` `UI Desktop` `popupMenuRMBTimerCB`;\
mapkey(continued) ~ Close `rmb_popup` `PopupMenu`;\
mapkey(continued) ~ Activate `rmb_popup` `DwgPopupFileProperties`;#DRAWING OPTIONS;\
mapkey(continued) ~ FocusOut `preferences` `InputOpt`;~ Activate `preferences` `Open`;\
mapkey(continued) ~ Select `file_open` `Ph_list.Filelist`1  `drawing.dtl`;\
mapkey(continued) ~ Activate `file_open` `Ph_list.Filelist`1  `drawing.dtl`;\
mapkey(continued) ~ Activate `preferences` `ok`;#DONE/RETURN;
template_sheetmetalpart /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/02-ProE-WF3-M100/stds/temp/mmks_part_sheetmetal.prt.5
browser_favorite /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE 
pro_font_dir /home/vladimir/Prace/ZIMA-Engineering/00-SOFTWARE/11-PTC/00-FONTS
display_points no

search_path /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE/02-PROJECTS/02-ACTIVE_PROJECTS/ZE0118-KIEKERT-UG845/import/KIEKERT/ABH/
search_path /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE/02-PROJECTS/02-ACTIVE_PROJECTS/ZE0118-KIEKERT-UG845/import/KIEKERT/ABH_ALH
search_path /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE/02-PROJECTS/02-ACTIVE_PROJECTS/ZE0118-KIEKERT-UG845/import/KIEKERT/Komplet_ridic
search_path /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE/02-PROJECTS/02-ACTIVE_PROJECTS/ZE0118-KIEKERT-UG845/import/KIEKERT/Komplet_zadni
search_path /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE/02-PROJECTS/02-ACTIVE_PROJECTS/ZE0118-KIEKERT-UG845/import/KIEKERT/SRB
search_path /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE/02-PROJECTS/02-ACTIVE_PROJECTS/ZE0118-KIEKERT-UG845/import/KIEKERT/ZVD_ridic
search_path /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE/02-PROJECTS/02-ACTIVE_PROJECTS/ZE0118-KIEKERT-UG845/import/KIEKERT/ZVD_spolujezdec
search_path /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE/02-PROJECTS/02-ACTIVE_PROJECTS/ZE0118-KIEKERT-UG845/import/KIEKERT/ZVD_zadni
search_path /home/vladimir/Prace/ZIMA-Engineering/03-WORKSPACE/02-PROJECTS/02-ACTIVE_PROJECTS/ZE0118-KIEKERT-UG845/import/BETZ/
