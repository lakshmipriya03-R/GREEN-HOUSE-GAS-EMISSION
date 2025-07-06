{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "675bde86-b07a-4a46-bab7-287583f88838",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Columns in the dataset:\n",
      "['Name', 'Supply Chain GHG Emission Factors for US Commodities and Industries']\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Step 1: Load dataset\n",
    "df = pd.read_excel(r\"C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx\")\n",
    "\n",
    "# Print the column names to verify\n",
    "print(\"✅ Columns in the dataset:\")\n",
    "print(df.columns.tolist())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "cb974dd7-ae7e-4183-8c89-44ab32bd8d32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Name Industry Code Industry Name Substance Unit Emission Factor  \\\n",
      "0      Authors           NaN           NaN       NaN  NaN             NaN   \n",
      "1  Description           NaN           NaN       NaN  NaN             NaN   \n",
      "2          DOI           NaN           NaN       NaN  NaN             NaN   \n",
      "\n",
      "  Margin  \n",
      "0    NaN  \n",
      "1    NaN  \n",
      "2    NaN  \n"
     ]
    }
   ],
   "source": [
    "# Step 2: Split the column into multiple structured columns\n",
    "df[['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin']] = df['Supply Chain GHG Emission Factors for US Commodities and Industries'].str.extract(\n",
    "    r'^(\\S+)\\s+(.*?)\\s{2,}([\\w\\s]+)\\s{2,}([a-zA-Z0-9/,\\s]+?)\\s+([\\d.]+)\\s+([\\d.]+)$'\n",
    ")\n",
    "\n",
    "# Drop the original combined column\n",
    "df = df.drop(columns=['Supply Chain GHG Emission Factors for US Commodities and Industries'])\n",
    "\n",
    "# Show first 5 rows to verify\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d1356753-26cd-4391-a9c4-29b209e7c3c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty DataFrame\n",
      "Columns: [Industry Code, Industry Name, Substance, Unit, Emission Factor, Margin]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "# Step 3: Remove metadata rows\n",
    "df = df[~df['Name'].isin(['Authors', 'Description', 'DOI'])].reset_index(drop=True)\n",
    "\n",
    "# Rerun the splitting logic again on cleaned data\n",
    "df[['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin']] = df['Name'].str.extract(\n",
    "    r'^(\\S+)\\s+(.*?)\\s{2,}([\\w\\s]+)\\s{2,}([a-zA-Z0-9/,\\s]+?)\\s+([\\d.]+)\\s+([\\d.]+)$'\n",
    ")\n",
    "\n",
    "# Drop the original messy column\n",
    "df = df.drop(columns=['Name'])\n",
    "\n",
    "# Display a few rows to confirm\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "5aaf862a-1a33-46cf-b279-2af104d2ad56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Columns: ['DOI', 'http://doi.org/10.23719/1517769']\n",
      "Number of columns: 2\n",
      "Empty DataFrame\n",
      "Columns: [DOI, http://doi.org/10.23719/1517769]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Step 1: Load Excel (skip top metadata rows)\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "df = pd.read_excel(file_path, skiprows=3)\n",
    "\n",
    "# Step 2: Print actual column names and number of columns\n",
    "print(\"Columns:\", df.columns.tolist())\n",
    "print(\"Number of columns:\", len(df.columns))\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "969b1e87-02e8-4694-8502-fbbed73fc53c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "             0                                                  1\n",
      "0         Name  Supply Chain GHG Emission Factors for US Commo...\n",
      "1      Authors                            Wesley Ingwersen, Mo Li\n",
      "2  Description  Tables presenting supply chain and margin emis...\n",
      "3          DOI                    http://doi.org/10.23719/1517769\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load Excel without skipping rows\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "df_raw = pd.read_excel(file_path, header=None)\n",
    "\n",
    "# Show the first 10 rows\n",
    "pd.set_option('display.max_columns', None)\n",
    "print(df_raw.head(10))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "27bde7b5-a7b5-4625-8cda-8e7eca27b3ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Columns: []\n",
      "✅ Preview:\n",
      "Empty DataFrame\n",
      "Columns: []\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load the file, skipping metadata rows\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "df = pd.read_excel(file_path, skiprows=4)\n",
    "\n",
    "# Show the real header and first few rows\n",
    "print(\"✅ Columns:\", df.columns.tolist())\n",
    "print(\"✅ Preview:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "22b2f64b-da37-4537-9896-008df49c05e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Columns: []\n",
      "✅ Preview:\n",
      "Empty DataFrame\n",
      "Columns: []\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Skip first 5 rows to reach the actual table\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "df = pd.read_excel(file_path, skiprows=5)\n",
    "\n",
    "# Show the real column names and first few rows\n",
    "print(\"✅ Columns:\", df.columns.tolist())\n",
    "print(\"✅ Preview:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "f1916d9a-09e7-4680-9a38-a0d69bb6f90d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "🔍 First 20 rows:\n",
      "Row 0: ['Name', 'Supply Chain GHG Emission Factors for US Commodities and Industries']\n",
      "Row 1: ['Authors', 'Wesley Ingwersen, Mo Li']\n",
      "Row 2: ['Description', 'Tables presenting supply chain and margin emission factors and data quality scores for US commodities and industries calculated from USEEIO models at two levels of commodity/industry categorization, detail and summary, for both industries and commodity, and annually from 2010-2016. See the EPA report for full details on emission factor preparation.']\n",
      "Row 3: ['DOI', 'http://doi.org/10.23719/1517769']\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "single positional indexer is out-of-bounds",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[26], line 9\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m🔍 First 20 rows:\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      8\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;241m20\u001b[39m):\n\u001b[1;32m----> 9\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRow \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mi\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mdf_raw\u001b[38;5;241m.\u001b[39miloc[i]\u001b[38;5;241m.\u001b[39mtolist()\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1191\u001b[0m, in \u001b[0;36m_LocationIndexer.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   1189\u001b[0m maybe_callable \u001b[38;5;241m=\u001b[39m com\u001b[38;5;241m.\u001b[39mapply_if_callable(key, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj)\n\u001b[0;32m   1190\u001b[0m maybe_callable \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_deprecated_callable_usage(key, maybe_callable)\n\u001b[1;32m-> 1191\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_getitem_axis(maybe_callable, axis\u001b[38;5;241m=\u001b[39maxis)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1752\u001b[0m, in \u001b[0;36m_iLocIndexer._getitem_axis\u001b[1;34m(self, key, axis)\u001b[0m\n\u001b[0;32m   1749\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCannot index by location index with a non-integer key\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m   1751\u001b[0m \u001b[38;5;66;03m# validate the location\u001b[39;00m\n\u001b[1;32m-> 1752\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_validate_integer(key, axis)\n\u001b[0;32m   1754\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj\u001b[38;5;241m.\u001b[39m_ixs(key, axis\u001b[38;5;241m=\u001b[39maxis)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1685\u001b[0m, in \u001b[0;36m_iLocIndexer._validate_integer\u001b[1;34m(self, key, axis)\u001b[0m\n\u001b[0;32m   1683\u001b[0m len_axis \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mlen\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj\u001b[38;5;241m.\u001b[39m_get_axis(axis))\n\u001b[0;32m   1684\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m key \u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m len_axis \u001b[38;5;129;01mor\u001b[39;00m key \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m-\u001b[39mlen_axis:\n\u001b[1;32m-> 1685\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mIndexError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msingle positional indexer is out-of-bounds\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mIndexError\u001b[0m: single positional indexer is out-of-bounds"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "df_raw = pd.read_excel(file_path, header=None)\n",
    "\n",
    "# Print the first 20 rows with row numbers\n",
    "print(\"\\n🔍 First 20 rows:\")\n",
    "for i in range(20):\n",
    "    print(f\"Row {i}: {df_raw.iloc[i].tolist()}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "a8e716a8-8003-46f2-a66f-6c2309dc9f89",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "✅ Columns:\n",
      "[]\n",
      "\n",
      "✅ Sample Data:\n",
      "Empty DataFrame\n",
      "Columns: []\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Skip metadata: Name, Authors, Description, DOI, Blank row\n",
    "df = pd.read_excel(file_path, skiprows=5)\n",
    "\n",
    "print(\"\\n✅ Columns:\")\n",
    "print(df.columns.tolist())\n",
    "\n",
    "print(\"\\n✅ Sample Data:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "96c6cc63-2319-4658-b537-cb260b1c62f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Row 0: ['Name', 'Supply Chain GHG Emission Factors for US Commodities and Industries']\n",
      "Row 1: ['Authors', 'Wesley Ingwersen, Mo Li']\n",
      "Row 2: ['Description', 'Tables presenting supply chain and margin emission factors and data quality scores for US commodities and industries calculated from USEEIO models at two levels of commodity/industry categorization, detail and summary, for both industries and commodity, and annually from 2010-2016. See the EPA report for full details on emission factor preparation.']\n",
      "Row 3: ['DOI', 'http://doi.org/10.23719/1517769']\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "single positional indexer is out-of-bounds",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[28], line 8\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[38;5;66;03m# Show first 20 rows with index\u001b[39;00m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;241m20\u001b[39m):\n\u001b[1;32m----> 8\u001b[0m     row_values \u001b[38;5;241m=\u001b[39m df_raw\u001b[38;5;241m.\u001b[39miloc[i]\u001b[38;5;241m.\u001b[39mtolist()\n\u001b[0;32m      9\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRow \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mi\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mrow_values\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1191\u001b[0m, in \u001b[0;36m_LocationIndexer.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   1189\u001b[0m maybe_callable \u001b[38;5;241m=\u001b[39m com\u001b[38;5;241m.\u001b[39mapply_if_callable(key, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj)\n\u001b[0;32m   1190\u001b[0m maybe_callable \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_deprecated_callable_usage(key, maybe_callable)\n\u001b[1;32m-> 1191\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_getitem_axis(maybe_callable, axis\u001b[38;5;241m=\u001b[39maxis)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1752\u001b[0m, in \u001b[0;36m_iLocIndexer._getitem_axis\u001b[1;34m(self, key, axis)\u001b[0m\n\u001b[0;32m   1749\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCannot index by location index with a non-integer key\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m   1751\u001b[0m \u001b[38;5;66;03m# validate the location\u001b[39;00m\n\u001b[1;32m-> 1752\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_validate_integer(key, axis)\n\u001b[0;32m   1754\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj\u001b[38;5;241m.\u001b[39m_ixs(key, axis\u001b[38;5;241m=\u001b[39maxis)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1685\u001b[0m, in \u001b[0;36m_iLocIndexer._validate_integer\u001b[1;34m(self, key, axis)\u001b[0m\n\u001b[0;32m   1683\u001b[0m len_axis \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mlen\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj\u001b[38;5;241m.\u001b[39m_get_axis(axis))\n\u001b[0;32m   1684\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m key \u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m len_axis \u001b[38;5;129;01mor\u001b[39;00m key \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m-\u001b[39mlen_axis:\n\u001b[1;32m-> 1685\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mIndexError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msingle positional indexer is out-of-bounds\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mIndexError\u001b[0m: single positional indexer is out-of-bounds"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "df_raw = pd.read_excel(file_path, header=None)\n",
    "\n",
    "# Show first 20 rows with index\n",
    "for i in range(20):\n",
    "    row_values = df_raw.iloc[i].tolist()\n",
    "    print(f\"Row {i}: {row_values}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "e3dae458-b7bf-4493-a7ea-d10a729a2f66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Columns in the dataset:\n",
      "[]\n",
      "\n",
      "✅ First few rows:\n",
      "Empty DataFrame\n",
      "Columns: []\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Skip metadata + blank rows → header is on row 5 (index 4), data starts from row 6\n",
    "df = pd.read_excel(file_path, skiprows=5)\n",
    "\n",
    "print(\"✅ Columns in the dataset:\")\n",
    "print(df.columns.tolist())\n",
    "\n",
    "print(\"\\n✅ First few rows:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "c8b26c4c-bfa3-4d3e-bc08-bf01c447effe",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "single positional indexer is out-of-bounds",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[30], line 9\u001b[0m\n\u001b[0;32m      6\u001b[0m df_raw \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(file_path, header\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m)\n\u001b[0;32m      8\u001b[0m \u001b[38;5;66;03m# Set the proper header row manually from row 5 (index 4)\u001b[39;00m\n\u001b[1;32m----> 9\u001b[0m new_header \u001b[38;5;241m=\u001b[39m df_raw\u001b[38;5;241m.\u001b[39miloc[\u001b[38;5;241m5\u001b[39m]\u001b[38;5;241m.\u001b[39mtolist()\n\u001b[0;32m     10\u001b[0m df \u001b[38;5;241m=\u001b[39m df_raw[\u001b[38;5;241m6\u001b[39m:]\u001b[38;5;241m.\u001b[39mcopy()\n\u001b[0;32m     11\u001b[0m df\u001b[38;5;241m.\u001b[39mcolumns \u001b[38;5;241m=\u001b[39m new_header\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1191\u001b[0m, in \u001b[0;36m_LocationIndexer.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   1189\u001b[0m maybe_callable \u001b[38;5;241m=\u001b[39m com\u001b[38;5;241m.\u001b[39mapply_if_callable(key, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj)\n\u001b[0;32m   1190\u001b[0m maybe_callable \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_deprecated_callable_usage(key, maybe_callable)\n\u001b[1;32m-> 1191\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_getitem_axis(maybe_callable, axis\u001b[38;5;241m=\u001b[39maxis)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1752\u001b[0m, in \u001b[0;36m_iLocIndexer._getitem_axis\u001b[1;34m(self, key, axis)\u001b[0m\n\u001b[0;32m   1749\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCannot index by location index with a non-integer key\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m   1751\u001b[0m \u001b[38;5;66;03m# validate the location\u001b[39;00m\n\u001b[1;32m-> 1752\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_validate_integer(key, axis)\n\u001b[0;32m   1754\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj\u001b[38;5;241m.\u001b[39m_ixs(key, axis\u001b[38;5;241m=\u001b[39maxis)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1685\u001b[0m, in \u001b[0;36m_iLocIndexer._validate_integer\u001b[1;34m(self, key, axis)\u001b[0m\n\u001b[0;32m   1683\u001b[0m len_axis \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mlen\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj\u001b[38;5;241m.\u001b[39m_get_axis(axis))\n\u001b[0;32m   1684\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m key \u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m len_axis \u001b[38;5;129;01mor\u001b[39;00m key \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m-\u001b[39mlen_axis:\n\u001b[1;32m-> 1685\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mIndexError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msingle positional indexer is out-of-bounds\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mIndexError\u001b[0m: single positional indexer is out-of-bounds"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Load without headers to inspect rows manually\n",
    "df_raw = pd.read_excel(file_path, header=None)\n",
    "\n",
    "# Set the proper header row manually from row 5 (index 4)\n",
    "new_header = df_raw.iloc[5].tolist()\n",
    "df = df_raw[6:].copy()\n",
    "df.columns = new_header\n",
    "\n",
    "print(\"✅ Fixed Columns:\")\n",
    "print(df.columns.tolist())\n",
    "\n",
    "print(\"\\n✅ Sample Data:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "df0611d2-54d7-47f6-b8c6-2219413a9c36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🔍 Total rows loaded: 4\n",
      "\n",
      "🧾 All rows:\n",
      "\n",
      "             0                                                  1\n",
      "0         Name  Supply Chain GHG Emission Factors for US Commo...\n",
      "1      Authors                            Wesley Ingwersen, Mo Li\n",
      "2  Description  Tables presenting supply chain and margin emis...\n",
      "3          DOI                    http://doi.org/10.23719/1517769\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "df_raw = pd.read_excel(file_path, header=None)\n",
    "\n",
    "print(f\"🔍 Total rows loaded: {len(df_raw)}\")\n",
    "print(\"\\n🧾 All rows:\\n\")\n",
    "print(df_raw)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b006957e-d49a-4366-85b0-fcb6aaa4b10a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "📄 Available sheets: ['Cover', 'Contents', 'Data Dictionary', 'Sources', 'LCIA Factors of Other GHGs', '2016_Summary_Commodity', '2015_Summary_Commodity', '2014_Summary_Commodity', '2013_Summary_Commodity', '2012_Summary_Commodity', '2011_Summary_Commodity', '2010_Summary_Commodity', '2016_Summary_Industry', '2015_Summary_Industry', '2014_Summary_Industry', '2013_Summary_Industry', '2012_Summary_Industry', '2011_Summary_Industry', '2010_Summary_Industry', '2016_Detail_Commodity', '2015_Detail_Commodity', '2014_Detail_Commodity', '2013_Detail_Commodity', '2012_Detail_Commodity', '2011_Detail_Commodity', '2010_Detail_Commodity', '2016_Detail_Industry', '2015_Detail_Industry', '2014_Detail_Industry', '2013_Detail_Industry', '2012_Detail_Industry', '2011_Detail_Industry', '2010_Detail_Industry', 'Sheet1']\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "xls = pd.ExcelFile(file_path)\n",
    "print(\"📄 Available sheets:\", xls.sheet_names)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "b61fb6a0-9e93-4785-bf29-eed1f3b7233e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                   Industry Name  \\\n",
      "0                                      Substance   \n",
      "1                                           Unit   \n",
      "2  Supply Chain Emission Factors without Margins   \n",
      "3       Margins of Supply Chain Emission Factors   \n",
      "4     Supply Chain Emission Factors with Margins   \n",
      "\n",
      "                                 Industry Name.1  \\\n",
      "0                                      Substance   \n",
      "1                                           Unit   \n",
      "2  Supply Chain Emission Factors without Margins   \n",
      "3       Margins of Supply Chain Emission Factors   \n",
      "4     Supply Chain Emission Factors with Margins   \n",
      "\n",
      "                                  Commodity Name  \\\n",
      "0                                      Substance   \n",
      "1                                           Unit   \n",
      "2  Supply Chain Emission Factors without Margins   \n",
      "3       Margins of Supply Chain Emission Factors   \n",
      "4     Supply Chain Emission Factors with Margins   \n",
      "\n",
      "                                Commodity Name.1  Unnamed: 4  Unnamed: 5  \\\n",
      "0                                      Substance         NaN         NaN   \n",
      "1                                           Unit         NaN         NaN   \n",
      "2  Supply Chain Emission Factors without Margins         NaN         NaN   \n",
      "3       Margins of Supply Chain Emission Factors         NaN         NaN   \n",
      "4     Supply Chain Emission Factors with Margins         NaN         NaN   \n",
      "\n",
      "   Unnamed: 6  Unnamed: 7                                      Substance  \\\n",
      "0         NaN         NaN                                           Unit   \n",
      "1         NaN         NaN  Supply Chain Emission Factors without Margins   \n",
      "2         NaN         NaN       Margins of Supply Chain Emission Factors   \n",
      "3         NaN         NaN     Supply Chain Emission Factors with Margins   \n",
      "4         NaN         NaN                                            NaN   \n",
      "\n",
      "  Unnamed: 9 Unnamed: 10 Unnamed: 11 Unnamed: 12  \\\n",
      "0        NaN         NaN         NaN         NaN   \n",
      "1        NaN         NaN         NaN         NaN   \n",
      "2        NaN         NaN         NaN         NaN   \n",
      "3        NaN         NaN         NaN         NaN   \n",
      "4        NaN         NaN         NaN         NaN   \n",
      "\n",
      "                                     Substance.1  \n",
      "0                                           Unit  \n",
      "1  Supply Chain Emission Factors without Margins  \n",
      "2       Margins of Supply Chain Emission Factors  \n",
      "3     Supply Chain Emission Factors with Margins  \n",
      "4                                            NaN  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Load the correct sheet, skip first 5 metadata rows\n",
    "df = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=5)\n",
    "\n",
    "# Clean column names\n",
    "df.columns = df.columns.str.strip()\n",
    "\n",
    "# Show preview\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "c879418f-4469-4112-aaee-9aff4ea079a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                          Unnamed: 8 Unnamed: 9 Unnamed: 10  \\\n",
      "0     DQ ReliabilityScore of Factors without Margins        NaN         NaN   \n",
      "1  DQ TemporalCorrelation of Factors without Margins        NaN         NaN   \n",
      "2  DQ GeographicalCorrelation of Factors without ...        NaN         NaN   \n",
      "3  DQ TechnologicalCorrelation of Factors without...        NaN         NaN   \n",
      "4       DQ DataCollection of Factors without Margins        NaN         NaN   \n",
      "\n",
      "  Unnamed: 11 Unnamed: 12                                        Unnamed: 13  \n",
      "0         NaN         NaN     DQ ReliabilityScore of Factors without Margins  \n",
      "1         NaN         NaN  DQ TemporalCorrelation of Factors without Margins  \n",
      "2         NaN         NaN  DQ GeographicalCorrelation of Factors without ...  \n",
      "3         NaN         NaN  DQ TechnologicalCorrelation of Factors without...  \n",
      "4         NaN         NaN       DQ DataCollection of Factors without Margins  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Skip top 10 rows (adjust if needed)\n",
    "df = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=10)\n",
    "\n",
    "# Drop fully empty columns\n",
    "df.dropna(axis=1, how='all', inplace=True)\n",
    "\n",
    "# Drop fully empty rows\n",
    "df.dropna(axis=0, how='all', inplace=True)\n",
    "\n",
    "# Clean column names\n",
    "df.columns = df.columns.str.strip()\n",
    "\n",
    "# Show first few rows\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "feb77441-fd4e-472f-95c5-003f357e944f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                      Unnamed: 0  \\\n",
      "0                                  Industry Code   \n",
      "1                                  Industry Name   \n",
      "2                                      Substance   \n",
      "3                                           Unit   \n",
      "4  Supply Chain Emission Factors without Margins   \n",
      "\n",
      "                                      Unnamed: 1  \\\n",
      "0                                  Industry Code   \n",
      "1                                  Industry Name   \n",
      "2                                      Substance   \n",
      "3                                           Unit   \n",
      "4  Supply Chain Emission Factors without Margins   \n",
      "\n",
      "                                      Unnamed: 2  \\\n",
      "0                                 Commodity Code   \n",
      "1                                 Commodity Name   \n",
      "2                                      Substance   \n",
      "3                                           Unit   \n",
      "4  Supply Chain Emission Factors without Margins   \n",
      "\n",
      "                                      Unnamed: 3  \\\n",
      "0                                 Commodity Code   \n",
      "1                                 Commodity Name   \n",
      "2                                      Substance   \n",
      "3                                           Unit   \n",
      "4  Supply Chain Emission Factors without Margins   \n",
      "\n",
      "                                   Industry Code Unnamed: 9 Unnamed: 10  \\\n",
      "0                                  Industry Name        NaN         NaN   \n",
      "1                                      Substance        NaN         NaN   \n",
      "2                                           Unit        NaN         NaN   \n",
      "3  Supply Chain Emission Factors without Margins        NaN         NaN   \n",
      "4       Margins of Supply Chain Emission Factors        NaN         NaN   \n",
      "\n",
      "  Unnamed: 11 Unnamed: 12                                 Commodity Code  \n",
      "0         NaN         NaN                                 Commodity Name  \n",
      "1         NaN         NaN                                      Substance  \n",
      "2         NaN         NaN                                           Unit  \n",
      "3         NaN         NaN  Supply Chain Emission Factors without Margins  \n",
      "4         NaN         NaN       Margins of Supply Chain Emission Factors  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Read the first 50 rows to find header\n",
    "preview = pd.read_excel(file_path, sheet_name=\"Sheet1\", nrows=50, header=None)\n",
    "\n",
    "# Find the header row where the actual data starts\n",
    "header_row_index = preview[preview.apply(lambda row: row.astype(str).str.contains(\"Industry Code\").any(), axis=1)].index[0]\n",
    "\n",
    "# Now load the real data from that row\n",
    "df = pd.read_excel(file_path, sheet_name=\"Sheet1\", skiprows=header_row_index)\n",
    "\n",
    "# Drop fully empty rows and columns\n",
    "df.dropna(axis=0, how='all', inplace=True)\n",
    "df.dropna(axis=1, how='all', inplace=True)\n",
    "\n",
    "# Clean column names\n",
    "df.columns = df.columns.str.strip()\n",
    "\n",
    "# Show preview\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "fb952e9f-0d11-47f9-8f09-5eb9ae926baa",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "index 0 is out of bounds for axis 0 with size 0",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[36], line 9\u001b[0m\n\u001b[0;32m      6\u001b[0m df_raw \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(file_path, sheet_name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mSheet1\u001b[39m\u001b[38;5;124m'\u001b[39m, header\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m)\n\u001b[0;32m      8\u001b[0m \u001b[38;5;66;03m# Find the first row where the first column contains '111CA' or any real Industry Code\u001b[39;00m\n\u001b[1;32m----> 9\u001b[0m start_row \u001b[38;5;241m=\u001b[39m df_raw[df_raw[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;241m.\u001b[39mastype(\u001b[38;5;28mstr\u001b[39m)\u001b[38;5;241m.\u001b[39mstr\u001b[38;5;241m.\u001b[39mstartswith(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m111\u001b[39m\u001b[38;5;124m'\u001b[39m)]\u001b[38;5;241m.\u001b[39mindex[\u001b[38;5;241m0\u001b[39m]\n\u001b[0;32m     11\u001b[0m \u001b[38;5;66;03m# Use that row as header\u001b[39;00m\n\u001b[0;32m     12\u001b[0m df \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(file_path, sheet_name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mSheet1\u001b[39m\u001b[38;5;124m'\u001b[39m, skiprows\u001b[38;5;241m=\u001b[39mstart_row \u001b[38;5;241m-\u001b[39m \u001b[38;5;241m1\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:5389\u001b[0m, in \u001b[0;36mIndex.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   5386\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m is_integer(key) \u001b[38;5;129;01mor\u001b[39;00m is_float(key):\n\u001b[0;32m   5387\u001b[0m     \u001b[38;5;66;03m# GH#44051 exclude bool, which would return a 2d ndarray\u001b[39;00m\n\u001b[0;32m   5388\u001b[0m     key \u001b[38;5;241m=\u001b[39m com\u001b[38;5;241m.\u001b[39mcast_scalar_indexer(key)\n\u001b[1;32m-> 5389\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m getitem(key)\n\u001b[0;32m   5391\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(key, \u001b[38;5;28mslice\u001b[39m):\n\u001b[0;32m   5392\u001b[0m     \u001b[38;5;66;03m# This case is separated from the conditional above to avoid\u001b[39;00m\n\u001b[0;32m   5393\u001b[0m     \u001b[38;5;66;03m# pessimization com.is_bool_indexer and ndim checks.\u001b[39;00m\n\u001b[0;32m   5394\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_getitem_slice(key)\n",
      "\u001b[1;31mIndexError\u001b[0m: index 0 is out of bounds for axis 0 with size 0"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Read whole sheet without headers\n",
    "df_raw = pd.read_excel(file_path, sheet_name='Sheet1', header=None)\n",
    "\n",
    "# Find the first row where the first column contains '111CA' or any real Industry Code\n",
    "start_row = df_raw[df_raw[0].astype(str).str.startswith('111')].index[0]\n",
    "\n",
    "# Use that row as header\n",
    "df = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=start_row - 1)\n",
    "\n",
    "# Drop empty rows and columns\n",
    "df.dropna(axis=0, how='all', inplace=True)\n",
    "df.dropna(axis=1, how='all', inplace=True)\n",
    "\n",
    "# Clean column names\n",
    "df.columns = df.columns.str.strip()\n",
    "\n",
    "# Print clean data\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "44b9ef8a-a3ad-45d7-bd48-09d378e94533",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'header_row' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[37], line 22\u001b[0m\n\u001b[0;32m     19\u001b[0m         \u001b[38;5;28;01mbreak\u001b[39;00m\n\u001b[0;32m     21\u001b[0m \u001b[38;5;66;03m# Now load real data using that row as header\u001b[39;00m\n\u001b[1;32m---> 22\u001b[0m df \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(file_path, sheet_name\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mSheet1\u001b[39m\u001b[38;5;124m'\u001b[39m, skiprows\u001b[38;5;241m=\u001b[39mheader_row)\n\u001b[0;32m     24\u001b[0m \u001b[38;5;66;03m# Drop empty rows/columns\u001b[39;00m\n\u001b[0;32m     25\u001b[0m df\u001b[38;5;241m.\u001b[39mdropna(axis\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0\u001b[39m, how\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mall\u001b[39m\u001b[38;5;124m'\u001b[39m, inplace\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'header_row' is not defined"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Load raw file without headers\n",
    "df_raw = pd.read_excel(file_path, sheet_name='Sheet1', header=None)\n",
    "\n",
    "# Find the header row containing all expected column names\n",
    "for i, row in df_raw.iterrows():\n",
    "    if (\n",
    "        \"Industry Code\" in row.values\n",
    "        and \"Industry Name\" in row.values\n",
    "        and \"Substance\" in row.values\n",
    "        and \"Unit\" in row.values\n",
    "        and \"Supply Chain Emission Factors without Margins\" in row.values\n",
    "        and \"Margins of Supply Chain Emission Factors\" in row.values\n",
    "    ):\n",
    "        header_row = i\n",
    "        break\n",
    "\n",
    "# Now load real data using that row as header\n",
    "df = pd.read_excel(file_path, sheet_name='Sheet1', skiprows=header_row)\n",
    "\n",
    "# Drop empty rows/columns\n",
    "df.dropna(axis=0, how='all', inplace=True)\n",
    "df.dropna(axis=1, how='all', inplace=True)\n",
    "\n",
    "# Clean column names\n",
    "df.columns = df.columns.str.strip()\n",
    "\n",
    "# Print first few rows to confirm\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "5f2318ac-094f-4b76-a935-3600e42ed16d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Row 0: ['2010_Detail_Industry', 1581, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 1: ['2010_Detail_Commodity', 265, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 2: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 3: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Industry Code', nan, nan, nan, nan, 'Commodity Code']\n",
      "Row 4: ['Industry Code', 'Industry Code', 'Commodity Code', 'Commodity Code', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Industry Name', nan, nan, nan, nan, 'Commodity Name']\n",
      "Row 5: ['Industry Name', 'Industry Name', 'Commodity Name', 'Commodity Name', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Substance', nan, nan, nan, nan, 'Substance']\n",
      "Row 6: ['Substance', 'Substance', 'Substance', 'Substance', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Unit', nan, nan, nan, nan, 'Unit']\n",
      "Row 7: ['Unit', 'Unit', 'Unit', 'Unit', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Supply Chain Emission Factors without Margins', nan, nan, nan, nan, 'Supply Chain Emission Factors without Margins']\n",
      "Row 8: ['Supply Chain Emission Factors without Margins', 'Supply Chain Emission Factors without Margins', 'Supply Chain Emission Factors without Margins', 'Supply Chain Emission Factors without Margins', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Margins of Supply Chain Emission Factors', nan, nan, nan, nan, 'Margins of Supply Chain Emission Factors']\n",
      "Row 9: ['Margins of Supply Chain Emission Factors', 'Margins of Supply Chain Emission Factors', 'Margins of Supply Chain Emission Factors', 'Margins of Supply Chain Emission Factors', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Supply Chain Emission Factors with Margins', nan, nan, nan, nan, 'Supply Chain Emission Factors with Margins']\n",
      "Row 10: ['Supply Chain Emission Factors with Margins', 'Supply Chain Emission Factors with Margins', 'Supply Chain Emission Factors with Margins', 'Supply Chain Emission Factors with Margins', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 11: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ ReliabilityScore of Factors without Margins', nan, nan, nan, nan, 'DQ ReliabilityScore of Factors without Margins']\n",
      "Row 12: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ TemporalCorrelation of Factors without Margins', nan, nan, nan, nan, 'DQ TemporalCorrelation of Factors without Margins']\n",
      "Row 13: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ GeographicalCorrelation of Factors without Margins', nan, nan, nan, nan, 'DQ GeographicalCorrelation of Factors without Margins']\n",
      "Row 14: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ TechnologicalCorrelation of Factors without Margins', nan, nan, nan, nan, 'DQ TechnologicalCorrelation of Factors without Margins']\n",
      "Row 15: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ DataCollection of Factors without Margins', nan, nan, nan, nan, 'DQ DataCollection of Factors without Margins']\n",
      "Row 16: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 17: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ ReliabilityScore of Factors without Margins', 'DQ TemporalCorrelation of Factors without Margins', 'DQ GeographicalCorrelation of Factors without Margins', 'DQ TechnologicalCorrelation of Factors without Margins', 'DQ DataCollection of Factors without Margins', nan]\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "single positional indexer is out-of-bounds",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[38], line 10\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[38;5;66;03m# Print first 20 rows to inspect the raw data\u001b[39;00m\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m i \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mrange\u001b[39m(\u001b[38;5;241m20\u001b[39m):\n\u001b[1;32m---> 10\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRow \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mi\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mdf_raw\u001b[38;5;241m.\u001b[39miloc[i]\u001b[38;5;241m.\u001b[39mtolist()\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1191\u001b[0m, in \u001b[0;36m_LocationIndexer.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   1189\u001b[0m maybe_callable \u001b[38;5;241m=\u001b[39m com\u001b[38;5;241m.\u001b[39mapply_if_callable(key, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj)\n\u001b[0;32m   1190\u001b[0m maybe_callable \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_deprecated_callable_usage(key, maybe_callable)\n\u001b[1;32m-> 1191\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_getitem_axis(maybe_callable, axis\u001b[38;5;241m=\u001b[39maxis)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1752\u001b[0m, in \u001b[0;36m_iLocIndexer._getitem_axis\u001b[1;34m(self, key, axis)\u001b[0m\n\u001b[0;32m   1749\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mTypeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mCannot index by location index with a non-integer key\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m   1751\u001b[0m \u001b[38;5;66;03m# validate the location\u001b[39;00m\n\u001b[1;32m-> 1752\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_validate_integer(key, axis)\n\u001b[0;32m   1754\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj\u001b[38;5;241m.\u001b[39m_ixs(key, axis\u001b[38;5;241m=\u001b[39maxis)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexing.py:1685\u001b[0m, in \u001b[0;36m_iLocIndexer._validate_integer\u001b[1;34m(self, key, axis)\u001b[0m\n\u001b[0;32m   1683\u001b[0m len_axis \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mlen\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mobj\u001b[38;5;241m.\u001b[39m_get_axis(axis))\n\u001b[0;32m   1684\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m key \u001b[38;5;241m>\u001b[39m\u001b[38;5;241m=\u001b[39m len_axis \u001b[38;5;129;01mor\u001b[39;00m key \u001b[38;5;241m<\u001b[39m \u001b[38;5;241m-\u001b[39mlen_axis:\n\u001b[1;32m-> 1685\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mIndexError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msingle positional indexer is out-of-bounds\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mIndexError\u001b[0m: single positional indexer is out-of-bounds"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Load without headers\n",
    "df_raw = pd.read_excel(file_path, sheet_name='Sheet1', header=None)\n",
    "\n",
    "# Print first 20 rows to inspect the raw data\n",
    "for i in range(20):\n",
    "    print(f\"Row {i}: {df_raw.iloc[i].tolist()}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "22f6b3b8-2b4c-4514-9317-0fd6d4d5f400",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Row 0: ['2010_Detail_Industry', 1581, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 1: ['2010_Detail_Commodity', 265, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 2: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 3: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Industry Code', nan, nan, nan, nan, 'Commodity Code']\n",
      "Row 4: ['Industry Code', 'Industry Code', 'Commodity Code', 'Commodity Code', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Industry Name', nan, nan, nan, nan, 'Commodity Name']\n",
      "Row 5: ['Industry Name', 'Industry Name', 'Commodity Name', 'Commodity Name', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Substance', nan, nan, nan, nan, 'Substance']\n",
      "Row 6: ['Substance', 'Substance', 'Substance', 'Substance', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Unit', nan, nan, nan, nan, 'Unit']\n",
      "Row 7: ['Unit', 'Unit', 'Unit', 'Unit', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Supply Chain Emission Factors without Margins', nan, nan, nan, nan, 'Supply Chain Emission Factors without Margins']\n",
      "Row 8: ['Supply Chain Emission Factors without Margins', 'Supply Chain Emission Factors without Margins', 'Supply Chain Emission Factors without Margins', 'Supply Chain Emission Factors without Margins', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Margins of Supply Chain Emission Factors', nan, nan, nan, nan, 'Margins of Supply Chain Emission Factors']\n",
      "Row 9: ['Margins of Supply Chain Emission Factors', 'Margins of Supply Chain Emission Factors', 'Margins of Supply Chain Emission Factors', 'Margins of Supply Chain Emission Factors', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'Supply Chain Emission Factors with Margins', nan, nan, nan, nan, 'Supply Chain Emission Factors with Margins']\n",
      "Row 10: ['Supply Chain Emission Factors with Margins', 'Supply Chain Emission Factors with Margins', 'Supply Chain Emission Factors with Margins', 'Supply Chain Emission Factors with Margins', np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 11: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ ReliabilityScore of Factors without Margins', nan, nan, nan, nan, 'DQ ReliabilityScore of Factors without Margins']\n",
      "Row 12: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ TemporalCorrelation of Factors without Margins', nan, nan, nan, nan, 'DQ TemporalCorrelation of Factors without Margins']\n",
      "Row 13: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ GeographicalCorrelation of Factors without Margins', nan, nan, nan, nan, 'DQ GeographicalCorrelation of Factors without Margins']\n",
      "Row 14: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ TechnologicalCorrelation of Factors without Margins', nan, nan, nan, nan, 'DQ TechnologicalCorrelation of Factors without Margins']\n",
      "Row 15: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ DataCollection of Factors without Margins', nan, nan, nan, nan, 'DQ DataCollection of Factors without Margins']\n",
      "Row 16: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), nan, nan, nan, nan, nan, nan]\n",
      "Row 17: [nan, nan, nan, nan, np.float64(nan), np.float64(nan), np.float64(nan), np.float64(nan), 'DQ ReliabilityScore of Factors without Margins', 'DQ TemporalCorrelation of Factors without Margins', 'DQ GeographicalCorrelation of Factors without Margins', 'DQ TechnologicalCorrelation of Factors without Margins', 'DQ DataCollection of Factors without Margins', nan]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Load without headers\n",
    "df_raw = pd.read_excel(file_path, sheet_name='Sheet1', header=None)\n",
    "\n",
    "# Print all available rows (up to 50 max)\n",
    "num_rows = min(len(df_raw), 50)\n",
    "for i in range(num_rows):\n",
    "    print(f\"Row {i}: {df_raw.iloc[i].tolist()}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "e7dbb012-18a8-4119-a158-dbbc83742edd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Loaded DataFrame with shape: (7, 10)\n",
      "✅ Columns: ['Margins of Supply Chain Emission Factors', 'Margins of Supply Chain Emission Factors.1', 'Margins of Supply Chain Emission Factors.2', 'Margins of Supply Chain Emission Factors.3', 'Supply Chain Emission Factors with Margins', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Supply Chain Emission Factors with Margins.1']\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load the Excel file with correct header row\n",
    "file_path = r'C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx'\n",
    "\n",
    "# Set header to row 10 (index 9), skip irrelevant top rows\n",
    "df = pd.read_excel(file_path, sheet_name='Sheet1', header=9)\n",
    "\n",
    "# Drop completely empty rows and columns\n",
    "df.dropna(axis=0, how='all', inplace=True)\n",
    "df.dropna(axis=1, how='all', inplace=True)\n",
    "\n",
    "# Show final columns and shape for verification\n",
    "print(\"✅ Loaded DataFrame with shape:\", df.shape)\n",
    "print(\"✅ Columns:\", df.columns.tolist())\n",
    "\n",
    "# Optional: Save cleaned data\n",
    "df.to_csv(\"cleaned_ghg.csv\", index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "ce29ab17-8ff2-4870-b01c-aa2689bbeebf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Final Cleaned Columns: ['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin']\n",
      "✅ Final Data Preview:\n",
      " Empty DataFrame\n",
      "Columns: [Industry Code, Industry Name, Substance, Unit, Emission Factor, Margin]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "# Rename confusing columns for clarity\n",
    "df.columns = [\n",
    "    'Industry Code',\n",
    "    'Industry Name',\n",
    "    'Substance',\n",
    "    'Unit',\n",
    "    'Emission Factor',\n",
    "    'Col6',\n",
    "    'Col7',\n",
    "    'Col8',\n",
    "    'Col9',\n",
    "    'Margin'\n",
    "]\n",
    "\n",
    "# Drop irrelevant columns (Col6 to Col9)\n",
    "df = df[['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin']]\n",
    "\n",
    "# Drop any rows with missing essential values\n",
    "df.dropna(subset=['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin'], inplace=True)\n",
    "\n",
    "print(\"✅ Final Cleaned Columns:\", df.columns.tolist())\n",
    "print(\"✅ Final Data Preview:\\n\", df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "cc546685-420a-4338-b254-a25dbea46fd3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Final Columns: ['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin']\n",
      "✅ Preview:\n",
      " Empty DataFrame\n",
      "Columns: [Industry Code, Industry Name, Substance, Unit, Emission Factor, Margin]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "# Rename only the actual existing columns safely\n",
    "df.rename(columns={\n",
    "    'Supply Chain Emission Factors without Margins': 'Emission Factor',\n",
    "    'Margins of Supply Chain Emission Factors': 'Margin'\n",
    "}, inplace=True)\n",
    "\n",
    "# Drop rows with missing essential info\n",
    "df.dropna(subset=['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin'], inplace=True)\n",
    "\n",
    "# Show final columns and preview\n",
    "print(\"✅ Final Columns:\", df.columns.tolist())\n",
    "print(\"✅ Preview:\\n\", df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "ced278b6-f06e-4e1f-894c-82bbbe6147b5",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin']",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp\\ipykernel_6840\\686811615.py\u001b[0m in \u001b[0;36m?\u001b[1;34m()\u001b[0m\n\u001b[0;32m      7\u001b[0m     \u001b[1;34m'Margins of Supply Chain Emission Factors'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m'Margin'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minplace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[1;31m# Drop rows with missing essential info\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdropna\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msubset\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'Industry Code'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'Industry Name'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'Substance'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'Unit'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'Emission Factor'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;34m'Margin'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0minplace\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;31m# Show final cleaned data\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     14\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"✅ Final Columns:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcolumns\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtolist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\frame.py\u001b[0m in \u001b[0;36m?\u001b[1;34m(self, axis, how, thresh, subset, inplace, ignore_index)\u001b[0m\n\u001b[0;32m   6666\u001b[0m             \u001b[0max\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_axis\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0magg_axis\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   6667\u001b[0m             \u001b[0mindices\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0max\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget_indexer_for\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msubset\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   6668\u001b[0m             \u001b[0mcheck\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mindices\u001b[0m \u001b[1;33m==\u001b[0m \u001b[1;33m-\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   6669\u001b[0m             \u001b[1;32mif\u001b[0m \u001b[0mcheck\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0many\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m-> 6670\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mnp\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marray\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msubset\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mcheck\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtolist\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m   6671\u001b[0m             \u001b[0magg_obj\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtake\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mindices\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0magg_axis\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   6672\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m   6673\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mthresh\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[0mlib\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mno_default\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: ['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin']"
     ]
    }
   ],
   "source": [
    "# Reload the file, skipping the first 3 metadata rows\n",
    "df = pd.read_excel(file_path, skiprows=3)\n",
    "\n",
    "# Rename correct columns\n",
    "df.rename(columns={\n",
    "    'Supply Chain Emission Factors without Margins': 'Emission Factor',\n",
    "    'Margins of Supply Chain Emission Factors': 'Margin'\n",
    "}, inplace=True)\n",
    "\n",
    "# Drop rows with missing essential info\n",
    "df.dropna(subset=['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Emission Factor', 'Margin'], inplace=True)\n",
    "\n",
    "# Show final cleaned data\n",
    "print(\"✅ Final Columns:\", df.columns.tolist())\n",
    "print(\"✅ Data Preview:\\n\", df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "3ce4dab4-508c-4194-bb3f-d7fbce41dc54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "📌 Raw Columns:\n",
      "- 'DOI'\n",
      "- 'http://doi.org/10.23719/1517769'\n"
     ]
    }
   ],
   "source": [
    "# Load skipping metadata rows\n",
    "df = pd.read_excel(file_path, skiprows=3)\n",
    "\n",
    "# Print actual column names as-is\n",
    "print(\"📌 Raw Columns:\")\n",
    "for col in df.columns:\n",
    "    print(f\"- '{col}'\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "a933c007-0502-4293-b752-4eeee82901bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Row 0: ['Authors', 'Wesley Ingwersen, Mo Li']\n",
      "Row 1: ['Description', 'Tables presenting supply chain and margin emission factors and data quality scores for US commodities and industries calculated from USEEIO models at two levels of commodity/industry categorization, detail and summary, for both industries and commodity, and annually from 2010-2016. See the EPA report for full details on emission factor preparation.']\n",
      "Row 2: ['DOI', 'http://doi.org/10.23719/1517769']\n"
     ]
    }
   ],
   "source": [
    "# Reload without skipping any rows\n",
    "df_raw = pd.read_excel(file_path)\n",
    "\n",
    "# Print first 30 rows as raw text\n",
    "for i in range(30):\n",
    "    try:\n",
    "        print(f\"Row {i}: {df_raw.iloc[i].tolist()}\")\n",
    "    except:\n",
    "        break\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "806a5c74-d5fd-45c2-bc60-4e9b2ce36d46",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Cleaned Columns:\n",
      "[]\n",
      "\n",
      "✅ Sample Rows:\n",
      "Empty DataFrame\n",
      "Columns: []\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Correct path to your file\n",
    "file_path = r\"C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx\"\n",
    "\n",
    "# Skip metadata rows and load actual data\n",
    "df = pd.read_excel(file_path, skiprows=4)\n",
    "\n",
    "# Show actual column names to verify\n",
    "print(\"✅ Cleaned Columns:\")\n",
    "print(df.columns.tolist())\n",
    "\n",
    "# Show first 5 rows to confirm structure\n",
    "print(\"\\n✅ Sample Rows:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "ac6dc591-2edc-4c84-9207-7e03ffd66519",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "📄 Sheet Names Found:\n",
      "['Cover', 'Contents', 'Data Dictionary', 'Sources', 'LCIA Factors of Other GHGs', '2016_Summary_Commodity', '2015_Summary_Commodity', '2014_Summary_Commodity', '2013_Summary_Commodity', '2012_Summary_Commodity', '2011_Summary_Commodity', '2010_Summary_Commodity', '2016_Summary_Industry', '2015_Summary_Industry', '2014_Summary_Industry', '2013_Summary_Industry', '2012_Summary_Industry', '2011_Summary_Industry', '2010_Summary_Industry', '2016_Detail_Commodity', '2015_Detail_Commodity', '2014_Detail_Commodity', '2013_Detail_Commodity', '2012_Detail_Commodity', '2011_Detail_Commodity', '2010_Detail_Commodity', '2016_Detail_Industry', '2015_Detail_Industry', '2014_Detail_Industry', '2013_Detail_Industry', '2012_Detail_Industry', '2011_Detail_Industry', '2010_Detail_Industry', 'Sheet1']\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "file_path = r\"C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx\"\n",
    "\n",
    "# List all available sheet names\n",
    "xls = pd.ExcelFile(file_path)\n",
    "print(\"📄 Sheet Names Found:\")\n",
    "print(xls.sheet_names)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "53c18683-4719-41cb-92d9-6dabe02eb095",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Columns:\n",
      "['1111A0', 'Oilseed farming', 'other GHGs', 'kg CO2e/2018 USD, purchaser price', 0.003, 0, '0.003.1', 'Unnamed: 7', 4, 2, 1, '4.1', '1.1']\n",
      "\n",
      "✅ Sample Data:\n",
      "   1111A0              Oilseed farming      other GHGs  \\\n",
      "0  1111B0                Grain farming  carbon dioxide   \n",
      "1  1111B0                Grain farming         methane   \n",
      "2  1111B0                Grain farming   nitrous oxide   \n",
      "3  1111B0                Grain farming      other GHGs   \n",
      "4  111200  Vegetable and melon farming  carbon dioxide   \n",
      "\n",
      "   kg CO2e/2018 USD, purchaser price  0.003      0  0.003.1  Unnamed: 7  4  2  \\\n",
      "0       kg/2018 USD, purchaser price  0.671  0.073    0.744         NaN  4  2   \n",
      "1       kg/2018 USD, purchaser price  0.006  0.001    0.007         NaN  2  2   \n",
      "2       kg/2018 USD, purchaser price  0.003  0.000    0.003         NaN  4  2   \n",
      "3  kg CO2e/2018 USD, purchaser price  0.004  0.000    0.004         NaN  4  2   \n",
      "4       kg/2018 USD, purchaser price  0.189  0.117    0.307         NaN  3  2   \n",
      "\n",
      "   1  4.1  1.1  \n",
      "0  1    4    1  \n",
      "1  1    1    1  \n",
      "2  1    4    1  \n",
      "3  1    4    1  \n",
      "4  1    4    1  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Path to your Excel file\n",
    "file_path = r\"C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx\"\n",
    "\n",
    "# Load the correct sheet (2016 detailed industry emissions)\n",
    "df = pd.read_excel(file_path, sheet_name=\"2016_Detail_Industry\", skiprows=4)\n",
    "\n",
    "# Show column names\n",
    "print(\"✅ Columns:\")\n",
    "print(df.columns.tolist())\n",
    "\n",
    "# Show sample rows\n",
    "print(\"\\n✅ Sample Data:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "5dadbe65-d900-4e2e-80fd-1c4c520a62e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Cleaned Data Columns:\n",
      "['Industry Code', 'Industry Name', 'Substance', 'Unit', 'Supply Chain Emission Factors without Margins', 'Margins of Supply Chain Emission Factors']\n",
      "\n",
      "✅ Sample Rows:\n",
      "   Industry Code    Industry Name       Substance  \\\n",
      "0  Industry Code    Industry Name       Substance   \n",
      "1         1111A0  Oilseed farming  carbon dioxide   \n",
      "2         1111A0  Oilseed farming         methane   \n",
      "3         1111A0  Oilseed farming   nitrous oxide   \n",
      "4         1111A0  Oilseed farming      other GHGs   \n",
      "\n",
      "                                Unit  \\\n",
      "0                               Unit   \n",
      "1       kg/2018 USD, purchaser price   \n",
      "2       kg/2018 USD, purchaser price   \n",
      "3       kg/2018 USD, purchaser price   \n",
      "4  kg CO2e/2018 USD, purchaser price   \n",
      "\n",
      "   Supply Chain Emission Factors without Margins  \\\n",
      "0  Supply Chain Emission Factors without Margins   \n",
      "1                                          0.332   \n",
      "2                                          0.001   \n",
      "3                                          0.002   \n",
      "4                                          0.003   \n",
      "\n",
      "   Margins of Supply Chain Emission Factors  \n",
      "0  Margins of Supply Chain Emission Factors  \n",
      "1                                     0.066  \n",
      "2                                     0.001  \n",
      "3                                         0  \n",
      "4                                         0  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Step 1: Load Excel with NO header (because the sheet has data, not column names)\n",
    "file_path = r\"C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx\"\n",
    "df_raw = pd.read_excel(file_path, sheet_name=\"2016_Detail_Industry\", header=None)\n",
    "\n",
    "# Step 2: Manually assign correct column names\n",
    "df_raw.columns = [\n",
    "    \"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\",\n",
    "    \"Supply Chain Emission Factors without Margins\",\n",
    "    \"Margins of Supply Chain Emission Factors\", \"Total Emission\",\n",
    "    \"Unnamed1\", \"Unnamed2\", \"Unnamed3\", \"Unnamed4\", \"Unnamed5\", \"Unnamed6\"\n",
    "]\n",
    "\n",
    "# Step 3: Drop unused columns\n",
    "df = df_raw[[\n",
    "    \"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\",\n",
    "    \"Supply Chain Emission Factors without Margins\",\n",
    "    \"Margins of Supply Chain Emission Factors\"\n",
    "]]\n",
    "\n",
    "# Step 4: Drop any rows with missing essential data\n",
    "df = df.dropna(subset=[\"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\"])\n",
    "\n",
    "# Step 5: Print to confirm\n",
    "print(\"✅ Cleaned Data Columns:\")\n",
    "print(df.columns.tolist())\n",
    "print(\"\\n✅ Sample Rows:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "3c28dfa1-d98a-492c-aa10-9414dd75f977",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndexError",
     "evalue": "index 0 is out of bounds for axis 0 with size 0",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[52], line 10\u001b[0m\n\u001b[0;32m      7\u001b[0m df_raw \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(file_path)\n\u001b[0;32m      9\u001b[0m \u001b[38;5;66;03m# Drop all rows until we hit the row where \"Industry Code\" is actually in the first column\u001b[39;00m\n\u001b[1;32m---> 10\u001b[0m start_index \u001b[38;5;241m=\u001b[39m df_raw[df_raw\u001b[38;5;241m.\u001b[39miloc[:, \u001b[38;5;241m0\u001b[39m] \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIndustry Code\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mindex[\u001b[38;5;241m0\u001b[39m] \u001b[38;5;241m+\u001b[39m \u001b[38;5;241m1\u001b[39m\n\u001b[0;32m     12\u001b[0m \u001b[38;5;66;03m# Re-read only the real data from that row onward\u001b[39;00m\n\u001b[0;32m     13\u001b[0m df_cleaned \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_excel(file_path, skiprows\u001b[38;5;241m=\u001b[39mstart_index)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\core\\indexes\\base.py:5389\u001b[0m, in \u001b[0;36mIndex.__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m   5386\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m is_integer(key) \u001b[38;5;129;01mor\u001b[39;00m is_float(key):\n\u001b[0;32m   5387\u001b[0m     \u001b[38;5;66;03m# GH#44051 exclude bool, which would return a 2d ndarray\u001b[39;00m\n\u001b[0;32m   5388\u001b[0m     key \u001b[38;5;241m=\u001b[39m com\u001b[38;5;241m.\u001b[39mcast_scalar_indexer(key)\n\u001b[1;32m-> 5389\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m getitem(key)\n\u001b[0;32m   5391\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(key, \u001b[38;5;28mslice\u001b[39m):\n\u001b[0;32m   5392\u001b[0m     \u001b[38;5;66;03m# This case is separated from the conditional above to avoid\u001b[39;00m\n\u001b[0;32m   5393\u001b[0m     \u001b[38;5;66;03m# pessimization com.is_bool_indexer and ndim checks.\u001b[39;00m\n\u001b[0;32m   5394\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_getitem_slice(key)\n",
      "\u001b[1;31mIndexError\u001b[0m: index 0 is out of bounds for axis 0 with size 0"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Full path to your dataset\n",
    "file_path = r\"C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx\"\n",
    "\n",
    "# Load raw file (don't skip any rows)\n",
    "df_raw = pd.read_excel(file_path)\n",
    "\n",
    "# Drop all rows until we hit the row where \"Industry Code\" is actually in the first column\n",
    "start_index = df_raw[df_raw.iloc[:, 0] == \"Industry Code\"].index[0] + 1\n",
    "\n",
    "# Re-read only the real data from that row onward\n",
    "df_cleaned = pd.read_excel(file_path, skiprows=start_index)\n",
    "\n",
    "# Rename columns properly\n",
    "df_cleaned.columns = [\n",
    "    \"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\",\n",
    "    \"Emission Factor\", \"Margin\"\n",
    "]\n",
    "\n",
    "# Drop any rows with all NaNs just in case\n",
    "df_cleaned.dropna(how=\"all\", inplace=True)\n",
    "\n",
    "# Reset index\n",
    "df_cleaned.reset_index(drop=True, inplace=True)\n",
    "\n",
    "# Debug: Show the cleaned data\n",
    "print(df_cleaned.head())\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "b70884d2-2998-4463-b56b-1f723848b455",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Cleaned Data Preview:\n",
      "  Industry Code    Industry Name       Substance  \\\n",
      "0        1111A0  Oilseed farming  carbon dioxide   \n",
      "1        1111A0  Oilseed farming         methane   \n",
      "2        1111A0  Oilseed farming   nitrous oxide   \n",
      "3        1111A0  Oilseed farming      other GHGs   \n",
      "4        1111B0    Grain farming  carbon dioxide   \n",
      "\n",
      "                                Unit  \\\n",
      "0       kg/2018 USD, purchaser price   \n",
      "1       kg/2018 USD, purchaser price   \n",
      "2       kg/2018 USD, purchaser price   \n",
      "3  kg CO2e/2018 USD, purchaser price   \n",
      "4       kg/2018 USD, purchaser price   \n",
      "\n",
      "  Supply Chain Emission Factors without Margins  \\\n",
      "0                                         0.332   \n",
      "1                                         0.001   \n",
      "2                                         0.002   \n",
      "3                                         0.003   \n",
      "4                                         0.671   \n",
      "\n",
      "  Margins of Supply Chain Emission Factors  \n",
      "0                                    0.066  \n",
      "1                                    0.001  \n",
      "2                                        0  \n",
      "3                                        0  \n",
      "4                                    0.073  \n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\84T g4\\AppData\\Local\\Temp\\ipykernel_6840\\339230462.py:26: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df.dropna(subset=[\"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\"], inplace=True)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Load raw Excel (header=None to avoid incorrect auto-columning)\n",
    "file_path = r\"C:\\Users\\84T g4\\Desktop\\GHG_Project\\greenhouse_gas.xlsx\"\n",
    "df_raw = pd.read_excel(file_path, sheet_name=\"2016_Detail_Industry\", header=None)\n",
    "\n",
    "# Assign correct column names manually\n",
    "df_raw.columns = [\n",
    "    \"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\",\n",
    "    \"Supply Chain Emission Factors without Margins\",\n",
    "    \"Margins of Supply Chain Emission Factors\", \"Total Emission\",\n",
    "    \"Unnamed1\", \"Unnamed2\", \"Unnamed3\", \"Unnamed4\", \"Unnamed5\", \"Unnamed6\"\n",
    "]\n",
    "\n",
    "# Drop the first row — it contains repeated fake headers\n",
    "df_raw = df_raw.iloc[1:].copy()\n",
    "\n",
    "# Keep only the required columns\n",
    "df = df_raw[[\n",
    "    \"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\",\n",
    "    \"Supply Chain Emission Factors without Margins\",\n",
    "    \"Margins of Supply Chain Emission Factors\"\n",
    "]]\n",
    "\n",
    "# Drop rows with any missing critical values\n",
    "df.dropna(subset=[\"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\"], inplace=True)\n",
    "\n",
    "# Reset index\n",
    "df.reset_index(drop=True, inplace=True)\n",
    "\n",
    "# Confirm it worked\n",
    "print(\"✅ Cleaned Data Preview:\")\n",
    "print(df.head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "0ef9b922-0ca6-41a5-aabf-8ae95e1c12f3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\84T g4\\AppData\\Local\\Temp\\ipykernel_6840\\939282187.py:9: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df[col] = enc.fit_transform(df[col])\n",
      "C:\\Users\\84T g4\\AppData\\Local\\Temp\\ipykernel_6840\\939282187.py:9: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df[col] = enc.fit_transform(df[col])\n",
      "C:\\Users\\84T g4\\AppData\\Local\\Temp\\ipykernel_6840\\939282187.py:9: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df[col] = enc.fit_transform(df[col])\n",
      "C:\\Users\\84T g4\\AppData\\Local\\Temp\\ipykernel_6840\\939282187.py:9: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  df[col] = enc.fit_transform(df[col])\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Model training complete and saved.\n"
     ]
    }
   ],
   "source": [
    "from sklearn.preprocessing import LabelEncoder\n",
    "from xgboost import XGBRegressor\n",
    "import joblib\n",
    "\n",
    "# Step 1: Encode categorical columns\n",
    "encoders = {}\n",
    "for col in [\"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\"]:\n",
    "    enc = LabelEncoder()\n",
    "    df[col] = enc.fit_transform(df[col])\n",
    "    encoders[col] = enc  # Save for future decoding\n",
    "\n",
    "# Step 2: Define features (X) and target (y)\n",
    "X = df[[\"Industry Code\", \"Industry Name\", \"Substance\", \"Unit\"]]\n",
    "y = df[\"Supply Chain Emission Factors without Margins\"].astype(float)\n",
    "\n",
    "# Step 3: Train XGBoost model\n",
    "model = XGBRegressor()\n",
    "model.fit(X, y)\n",
    "\n",
    "# Step 4: Save model and encoders\n",
    "joblib.dump(model, \"ghg_model.pkl\")\n",
    "joblib.dump(encoders, \"ghg_encoders.pkl\")\n",
    "\n",
    "print(\"✅ Model training complete and saved.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfd35a86-0f3a-4ee1-a46c-2a5e7eb0f9ff",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
