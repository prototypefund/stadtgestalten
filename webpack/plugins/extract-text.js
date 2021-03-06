const ExtractTextPlugin = require('extract-text-webpack-plugin')

const extractText = new ExtractTextPlugin({
  filename: '[contenthash].css'
})

extractText.lessConfig = {
  test: /\.less$/,
  use: extractText.extract({
    use: [
      {
        loader: 'css-loader',
        options: {
          sourceMap: true
        }
      },
      {
        loader: 'postcss-loader',
        options: {
          sourceMap: true
        }
      },
      {
        loader: 'less-loader',
        options: {
          sourceMap: true,
          strictMath: true,
          strictUnits: true,
          noIeCompat: true,
          compress: false,
          outputSourceFiles: true,
          sourceMapFileInline: true
        }
      }
    ]
  })
}

module.exports = extractText
