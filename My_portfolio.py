{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "05267b82",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-01-20 15:14:55.862 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run c:\\Users\\student\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-01-20 15:14:55.866 Session state does not function when running a script without `streamlit run`\n"
     ]
    },
    {
     "ename": "RuntimeError",
     "evalue": "Runtime hasn't been created!",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "File \u001b[1;32mc:\\Users\\student\\anaconda3\\Lib\\site-packages\\streamlit\\elements\\image.py:386\u001b[0m, in \u001b[0;36mimage_to_url\u001b[1;34m(image, width, clamp, channels, output_format, image_id)\u001b[0m\n\u001b[0;32m    385\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 386\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(image, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[0;32m    387\u001b[0m         image_data \u001b[38;5;241m=\u001b[39m f\u001b[38;5;241m.\u001b[39mread()\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'portfolio_banner.png'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 17\u001b[0m\n\u001b[0;32m     12\u001b[0m     st\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mWelcome to Vedaste\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124ms Portfolio\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     13\u001b[0m     st\u001b[38;5;241m.\u001b[39mwrite(\u001b[38;5;124m\"\"\"\u001b[39m\n\u001b[0;32m     14\u001b[0m \u001b[38;5;124m    Hello! I\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mm Vedaste, an Applied Mathematics student and data enthusiast.\u001b[39m\n\u001b[0;32m     15\u001b[0m \u001b[38;5;124m    I work on Machine Learning, Data Analysis, and Mathematical Modeling projects.\u001b[39m\n\u001b[0;32m     16\u001b[0m \u001b[38;5;124m    \u001b[39m\u001b[38;5;124m\"\"\"\u001b[39m)\n\u001b[1;32m---> 17\u001b[0m     st\u001b[38;5;241m.\u001b[39mimage(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mportfolio_banner.png\u001b[39m\u001b[38;5;124m\"\u001b[39m, use_column_width\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)  \u001b[38;5;66;03m# Add a banner image here\u001b[39;00m\n\u001b[0;32m     19\u001b[0m \u001b[38;5;66;03m# --- Projects Page ---\u001b[39;00m\n\u001b[0;32m     20\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m page \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mProjects\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n",
      "File \u001b[1;32mc:\\Users\\student\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\metrics_util.py:408\u001b[0m, in \u001b[0;36mgather_metrics.<locals>.wrapped_func\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    406\u001b[0m         _LOGGER\u001b[38;5;241m.\u001b[39mdebug(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFailed to collect command telemetry\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39mex)\n\u001b[0;32m    407\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 408\u001b[0m     result \u001b[38;5;241m=\u001b[39m non_optional_func(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n\u001b[0;32m    409\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m RerunException \u001b[38;5;28;01mas\u001b[39;00m ex:\n\u001b[0;32m    410\u001b[0m     \u001b[38;5;66;03m# Duplicated from below, because static analysis tools get confused\u001b[39;00m\n\u001b[0;32m    411\u001b[0m     \u001b[38;5;66;03m# by deferring the rethrow.\u001b[39;00m\n\u001b[0;32m    412\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m tracking_activated \u001b[38;5;129;01mand\u001b[39;00m command_telemetry:\n",
      "File \u001b[1;32mc:\\Users\\student\\anaconda3\\Lib\\site-packages\\streamlit\\elements\\image.py:161\u001b[0m, in \u001b[0;36mImageMixin.image\u001b[1;34m(self, image, caption, width, use_column_width, clamp, channels, output_format)\u001b[0m\n\u001b[0;32m    158\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StreamlitAPIException(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mImage width must be positive.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    160\u001b[0m image_list_proto \u001b[38;5;241m=\u001b[39m ImageListProto()\n\u001b[1;32m--> 161\u001b[0m marshall_images(\n\u001b[0;32m    162\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdg\u001b[38;5;241m.\u001b[39m_get_delta_path_str(),\n\u001b[0;32m    163\u001b[0m     image,\n\u001b[0;32m    164\u001b[0m     caption,\n\u001b[0;32m    165\u001b[0m     width,\n\u001b[0;32m    166\u001b[0m     image_list_proto,\n\u001b[0;32m    167\u001b[0m     clamp,\n\u001b[0;32m    168\u001b[0m     channels,\n\u001b[0;32m    169\u001b[0m     output_format,\n\u001b[0;32m    170\u001b[0m )\n\u001b[0;32m    171\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdg\u001b[38;5;241m.\u001b[39m_enqueue(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mimgs\u001b[39m\u001b[38;5;124m\"\u001b[39m, image_list_proto)\n",
      "File \u001b[1;32mc:\\Users\\student\\anaconda3\\Lib\\site-packages\\streamlit\\elements\\image.py:551\u001b[0m, in \u001b[0;36mmarshall_images\u001b[1;34m(coordinates, image, caption, width, proto_imgs, clamp, channels, output_format)\u001b[0m\n\u001b[0;32m    547\u001b[0m \u001b[38;5;66;03m# We use the index of the image in the input image list to identify this image inside\u001b[39;00m\n\u001b[0;32m    548\u001b[0m \u001b[38;5;66;03m# MediaFileManager. For this, we just add the index to the image's \"coordinates\".\u001b[39;00m\n\u001b[0;32m    549\u001b[0m image_id \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m-\u001b[39m\u001b[38;5;132;01m%i\u001b[39;00m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m%\u001b[39m (coordinates, coord_suffix)\n\u001b[1;32m--> 551\u001b[0m proto_img\u001b[38;5;241m.\u001b[39murl \u001b[38;5;241m=\u001b[39m image_to_url(\n\u001b[0;32m    552\u001b[0m     image, width, clamp, channels, output_format, image_id\n\u001b[0;32m    553\u001b[0m )\n",
      "File \u001b[1;32mc:\\Users\\student\\anaconda3\\Lib\\site-packages\\streamlit\\elements\\image.py:398\u001b[0m, in \u001b[0;36mimage_to_url\u001b[1;34m(image, width, clamp, channels, output_format, image_id)\u001b[0m\n\u001b[0;32m    395\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m mimetype \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    396\u001b[0m     mimetype \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mapplication/octet-stream\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m--> 398\u001b[0m url \u001b[38;5;241m=\u001b[39m runtime\u001b[38;5;241m.\u001b[39mget_instance()\u001b[38;5;241m.\u001b[39mmedia_file_mgr\u001b[38;5;241m.\u001b[39madd(image, mimetype, image_id)\n\u001b[0;32m    399\u001b[0m caching\u001b[38;5;241m.\u001b[39msave_media_data(image, mimetype, image_id)\n\u001b[0;32m    400\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m url\n",
      "File \u001b[1;32mc:\\Users\\student\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\__init__.py:28\u001b[0m, in \u001b[0;36mget_instance\u001b[1;34m()\u001b[0m\n\u001b[0;32m     24\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mget_instance\u001b[39m() \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Runtime:\n\u001b[0;32m     25\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Return the singleton Runtime instance. Raise an Error if the\u001b[39;00m\n\u001b[0;32m     26\u001b[0m \u001b[38;5;124;03m    Runtime hasn't been created yet.\u001b[39;00m\n\u001b[0;32m     27\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m---> 28\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m Runtime\u001b[38;5;241m.\u001b[39minstance()\n",
      "File \u001b[1;32mc:\\Users\\student\\anaconda3\\Lib\\site-packages\\streamlit\\runtime\\runtime.py:161\u001b[0m, in \u001b[0;36mRuntime.instance\u001b[1;34m(cls)\u001b[0m\n\u001b[0;32m    157\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Return the singleton Runtime instance. Raise an Error if the\u001b[39;00m\n\u001b[0;32m    158\u001b[0m \u001b[38;5;124;03mRuntime hasn't been created yet.\u001b[39;00m\n\u001b[0;32m    159\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    160\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mcls\u001b[39m\u001b[38;5;241m.\u001b[39m_instance \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m--> 161\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRuntime hasn\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt been created!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    162\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mcls\u001b[39m\u001b[38;5;241m.\u001b[39m_instance\n",
      "\u001b[1;31mRuntimeError\u001b[0m: Runtime hasn't been created!"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# --- Sidebar / Navigation ---\n",
    "st.sidebar.title(\"Navigation\")\n",
    "page = st.sidebar.radio(\"Go to\", [\"Home\", \"Projects\", \"About Me\", \"Contact\"])\n",
    "\n",
    "# --- Home Page ---\n",
    "if page == \"Home\":\n",
    "    st.title(\"Welcome to Vedaste's Portfolio\")\n",
    "    st.write(\"\"\"\n",
    "    Hello! I'm Vedaste, an Applied Mathematics student and data enthusiast.\n",
    "    I work on Machine Learning, Data Analysis, and Mathematical Modeling projects.\n",
    "    \"\"\")\n",
    "    st.image(\"portfolio_banner.png\", use_column_width=True)  # Add a banner image here\n",
    "\n",
    "# --- Projects Page ---\n",
    "elif page == \"Projects\":\n",
    "    st.title(\"My Projects\")\n",
    "\n",
    "    # Project 1\n",
    "    st.subheader(\"1. Student Depression Prediction\")\n",
    "    st.write(\"\"\"\n",
    "    Using Machine Learning to predict depression levels in students based on survey data.\n",
    "    Tools: Python, Pandas, Scikit-learn, Seaborn, Matplotlib\n",
    "    \"\"\")\n",
    "    st.image(\"depression_project.png\", caption=\"Depression Prediction Chart\")  # Add project image\n",
    "\n",
    "    # Example interactive chart\n",
    "    st.write(\"Sample Visualization:\")\n",
    "    data = pd.DataFrame({\n",
    "        'Months': ['Jan', 'Feb', 'Mar', 'Apr'],\n",
    "        'Depression_Score': [5, 6, 4, 7]\n",
    "    })\n",
    "    st.line_chart(data.set_index('Months'))\n",
    "\n",
    "    # Project 2\n",
    "    st.subheader(\"2. SEITRD TB Model for Rwanda\")\n",
    "    st.write(\"\"\"\n",
    "    Mathematical modeling of Tuberculosis spread using a SEITRD compartmental model.\n",
    "    Tools: Python, Matplotlib, Numpy\n",
    "    \"\"\")\n",
    "    st.image(\"tb_model.png\", caption=\"TB Model Simulation\")  # Add project image\n",
    "\n",
    "# --- About Me Page ---\n",
    "elif page == \"About Me\":\n",
    "    st.title(\"About Me\")\n",
    "    st.write(\"\"\"\n",
    "    I'm a Year 2 Applied Mathematics student at the University of Rwanda.\n",
    "    My interests:\n",
    "    - Mathematical modeling (SEIR, SEITRD, etc.)\n",
    "    - Machine Learning & AI\n",
    "    - Data Analysis & Visualization\n",
    "    \"\"\")\n",
    "    st.image(\"me.png\", caption=\"That's me!\")\n",
    "\n",
    "# --- Contact Page ---\n",
    "elif page == \"Contact\":\n",
    "    st.title(\"Contact Me\")\n",
    "    st.write(\"You can reach me via:\")\n",
    "    st.write(\"- Email: vedaste@example.com\")\n",
    "    st.write(\"- LinkedIn: [Your LinkedIn](https://linkedin.com)\")\n",
    "    st.write(\"- GitHub: [My GitHub](https://github.com/Vedaste-bit)\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
