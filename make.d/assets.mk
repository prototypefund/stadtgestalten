DIR_STATIC = $(DIR_BUILD)/static
DIR_RES = res
DIR_FONTS = $(DIR_RES)/fonts
DIR_NODE = node_modules
DIR_NODE_BIN ?= $(DIR_NODE)/.bin

BIN_STANDARD = $(DIR_NODE_BIN)/standard
BIN_WEBPACK = $(DIR_NODE_BIN)/webpack
BIN_FONTDUMP = $(DIR_NODE_BIN)/fontdump

DEPS_ASSETS = $(shell find "$(DIR_RES)" -type f)
DEPS_FONTS = $(shell find "$(DIR_FONTS)" -type f)
DEPS_WEBPACK = $(shell find "webpack" -type f)

# intermediate build files
BUILD_FONT_GOOGLE = $(DIR_BUILD)/fonts/google

# static output files
DIR_STATIC_FONT = $(DIR_STATIC)/fonts
DIR_STATIC_FONT_GOOGLE = $(DIR_STATIC_FONT)/google
STAMP_STATIC_FONT_GOOGLE = $(DIR_BUILD)/.static_font_google
STAMP_STATIC_WEBPACK = $(DIR_BUILD)/.static_webpack

URL_FONT_GOOGLE = https://fonts.googleapis.com/css?family=Roboto+Slab:300,400,700|Roboto:300,400,400i,500,700

$(DIR_NODE): $(BIN_NODE) package.json
	$(RUN_NODE) "$(BIN_NODE_PKG)" ci --no-progress
	touch -c "$(DIR_NODE)"

$(STAMP_STATIC_FONT_GOOGLE): $(DIR_NODE)
	mkdir -p "$(BUILD_FONT_GOOGLE)"
	$(RUN_NODE) "$(BIN_FONTDUMP)" --target-directory "$(BUILD_FONT_GOOGLE)" --web-directory "." "$(URL_FONT_GOOGLE)"
	mkdir -p "$(DIR_STATIC_FONT_GOOGLE)"
	cp -a --target-directory "$(DIR_STATIC_FONT_GOOGLE)" \
		"$(BUILD_FONT_GOOGLE)"/*.eot \
		"$(BUILD_FONT_GOOGLE)"/*.svg \
		"$(BUILD_FONT_GOOGLE)"/*.ttf \
		"$(BUILD_FONT_GOOGLE)"/*.woff \
		"$(BUILD_FONT_GOOGLE)"/*.woff2
	touch "$(STAMP_STATIC_FONT_GOOGLE)"

$(STAMP_STATIC_WEBPACK): $(STAMP_STATIC_FONT_GOOGLE) $(DEPS_ASSETS) $(DEPS_WEBPACK)
	mkdir -p "$(DIR_STATIC)"
	NODE_ENV=production $(RUN_NODE) $(BIN_WEBPACK) --bail
	touch "$(STAMP_STATIC_WEBPACK)"

.PHONY: assets_fonts
assets_fonts: $(STAMP_STATIC_FONT_GOOGLE)

.PHONY: assets_webpack
assets_webpack: $(STAMP_STATIC_WEBPACK)

.PHONY: assets
assets: assets_fonts assets_webpack
