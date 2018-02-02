
import glob




if __name__ is "__main__":
	folder_name = "cnn_data"
	text = ""
	for filename in glob.glob('news_scraper/' + folder_name + "/*.txt'):
		with open(filename) as f:
		    lines = f.readlines()
		text= text.join(lines)

	print("DATA LOADED")
	print("CHARACTER LENGTH: ", len(text))

	# Generate a word cloud image
	wordcloud = WordCloud().generate(text)

	# Display the generated image:
	# the matplotlib way:
	import matplotlib.pyplot as plt
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")

	# lower max_font_size
	wordcloud = WordCloud(max_font_size=40).generate(text)
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.show()

	# The pil way (if you don't have matplotlib)
	# image = wordcloud.to_image()
	# image.show()